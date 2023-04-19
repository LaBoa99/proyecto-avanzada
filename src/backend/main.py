from flask import Flask
from hello_controller import hello

app = Flask(__name__)
# Controllers
app.register_blueprint(hello)

if __name__ == "__main__":
    app.run()
