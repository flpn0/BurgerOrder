from flask import Flask, render_template
app = Flask(__name__, static_url_path="Burger.css")

@app.route("/")
def home():
    with open('Burger.html', 'r') as fp:
        html = fp.read()
    return html

@app.route("/buy")
def hello_mans():
    with open('Burger.html', 'r') as fp:
        html = fp.read()
    return "kj"
