from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_mons():
    with open('Burger.html', 'r') as fp:
        html = fp.read()
    return html

@app.route("/buy")
def hello_mans():
    with open('Burger.html', 'r') as fp:
        html = fp.read()
    return "kj"