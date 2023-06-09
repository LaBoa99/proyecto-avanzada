from flask import Blueprint, jsonify, request


class Route:
    @staticmethod
    def registerCRUD(blue_print: Blueprint, controller, instance: str):
        blue_print.add_url_rule(
            "/<int:id>", instance, controller.getOne, methods=["GET"]
        )
        blue_print.add_url_rule(
            "/", instance + "/create", controller.add, methods=["POST"]
        )
        blue_print.add_url_rule(
            "/<int:id>", instance + "/update", controller.updateWithID, methods=["PUT"]
        )
        blue_print.add_url_rule(
            "/<int:id>",
            instance + "/delete",
            controller.destroyWithID,
            methods=["DELETE"],
        )
        blue_print.add_url_rule("/", "", controller.getAll, methods=["GET"])
