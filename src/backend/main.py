from flask import Flask, jsonify

from hello_controller import hello_blueprint


app = Flask(__name__)


# Rutas
app.register_blueprint(hello_blueprint, url_prefix="/hellos")

if __name__ == "__main__":
    app.run()
