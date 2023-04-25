from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Je serais dû pour des Hot Dog sul BBQ"

