from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("Burger.html")

@app.route("/oder.html")
def hello_mans():
    return render_template("oder.html")

if __name__ == "__main__":
    app.run(debug=True)  