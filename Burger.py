from flask import Flask, render_template
from flask import request
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("Burger.html")

def oder_post():
    print(request.form)
    return request.form

@app.route("/oder.html", methods=["GET", "POST"])
def oder():
    if request.method == "POST":
        return oder_post()
    return render_template("oder.html")

if __name__ == "__main__":
    app.run(debug=True)  