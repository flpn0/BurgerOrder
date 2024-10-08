from flask import Flask, render_template
from flask import request
app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("MenuStore.html")

def order_post():
    print(request.form)
    return request.form

@app.route("/BurgerOrderer.html", methods=["GET", "POST"])
def oder():
    if request.method == "POST":
        return order_post()
    return render_template("BurgerOrderer.html")

if __name__ == "__main__":
    app.run(debug=True)  