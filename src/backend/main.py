from flask import Flask

from hello_controller import hello_blueprint


app = Flask(__name__)
# Controllers
app.register_blueprint(hello_blueprint, url_prefix="/hellos")

if __name__ == "__main__":
    app.run()
    
