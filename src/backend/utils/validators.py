from functools import wraps
import re
from typing import Type, Dict, Any

from werkzeug.exceptions import BadRequest
from flask import jsonify, request

"""
    SIMBOLOS
    ne = no igual a 
    gt = mayor que
    lt = menor que
    ge = mayor o igual a
    le = menor o iagual a 
    
    asc = ascendiente
    des = descendiente
    
    PARAMETROS DE EDICION
    filter 
    select
    order

"""


class Validators:
    @staticmethod
    def validate_query_params(columns: list[str] | dict):
        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                allowed_keys = {"select", "filter", "order"}
                allowed_operators = ["ne", "gt", "lt", "ge", "le"]
                allowed_order_by = ["asc", "desc"]

                params = list(request.args.keys())
                if len(params) == 0:
                    return f(*args, **kwargs)

                if not allowed_keys.issuperset(set(params)):
                    raise BadRequest("los parametros no son validos")

                select = request.args.get("select")
                filter = request.args.get("filter")
                orderby = request.args.get("order")
                query_config = {}

                preparedColums = columns.keys() if type(columns) == dict else columns
                if select:
                    isOK = all(param in preparedColums for param in select.split(","))
                    if not isOK:
                        print("aqui hay un error")
                        raise BadRequest("No son validos los parametros")
                    query_config["select"] = select
                if filter:
                    filters = filter.split(",")
                    tempFilter = []
                    for filter in filters:
                        key, operator, value = filter.split(" ")
                        if Validators.check_query(
                            key, operator, preparedColums, allowed_operators, value
                        ):
                            tempFilter.append([key, operator, value])
                    if len(tempFilter) > 0:
                        query_config["filter"] = tempFilter
                if orderby:
                    orders = orderby.split(",")
                    tempOrderBy = []
                    for order in orders:
                        key, operator, value = order.split(" ")
                        if Validators.check_query(
                            key, operator, preparedColums, allowed_order_by, value
                        ):
                            tempOrderBy.append([key, operator, value])
                    if len(tempOrderBy) > 0:
                        query_config["order"] = tempOrderBy
                setattr(request, "query_config", query_config)
                return f(*args, **kwargs)

            return wrapper

        return decorator

    @staticmethod
    def validate_response(properties):
        def decorator(f):
            @wraps(f)
            def wrapper(*args, **kwargs):
                data = request.get_json()

                # Se hace una funcion anonima para hacer recursividad.
                def check_instances(request, template: Dict[str, Dict[str, Any]]):
                    if not isinstance(request, dict):
                        raise BadRequest(
                            "La respuesta no es un objeto JSON o no es valido"
                        )
                    for key, value in request.items():
                        if key not in template and not template[key]["optional"]:
                            raise BadRequest(
                                f'la propiedad "{key}" no esta presente en la respuesta'
                            )
                        if type(value) != template[key]["type"]:
                            raise BadRequest(f'la propeida "{key} noe s del mismo tipo')
                        if type(value) == dict:
                            check_instances(request[key], template[key])

                        # elif value['type'] == list:
                        #     if not all(type(x) == type(value[0]) for x in request[key]):
                        #         raise BadRequest(
                        #             f'la propiedad "{key}" no esta presente en la respuesta'
                        #         )

                    return request

                check_instances(data, properties)
                return f(*args, **kwargs)

            return wrapper

        return decorator

    @staticmethod
    def check_query(key, operator, columns, allowed_operators, value):
        return key in columns and operator in allowed_operators and value != None
