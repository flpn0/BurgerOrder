from flask import Flask, render_template, session, request, make_response
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
app = Flask(__name__, template_folder='templates')

class Order(Base):
    __tablename__ = "orders"

    id = Column("id", Integer, primary_key=True)
    cheese = Column("cheese", Integer)
    dressing = Column("dressing", Integer)
    onion = Column("onion", Integer)
    patty = Column("patty", Integer)
    pickles = Column("pickles", Integer)

    def __init__(self, cheese, dressing, onion, patty, pickles):
        self.cheese = cheese
        self.dressing = dressing
        self.onion = onion
        self.patty = patty
        self.pickles = pickles

    def __repr__(self):
        personal_order = f"{self.cheese}, {self.dressing}, {self.onion}, {self.patty}, {self.pickles}"
        return personal_order
    
engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def home():
    return render_template("StartMenu.html")

def order_post():
    print(request.form)
    return request.form

@app.route("/BurgerOrderer.html", methods=["GET", "POST"])
def MenuStore():
    if request.method == "POST":

        cheese = request.form.get("cheese")
        dressing = request.form.get("dressing")
        onion = request.form.get("onion")
        patty = request.form.get("patty")
        pickles = request.form.get("pickles")

        order = Order(cheese, dressing, onion, patty, pickles)
        session.add(order)
        session.commit()
        order_id = order.id
    
        resp = make_response(order_confirmation(order_id))
        resp.set_cookie("cheese", cheese)
        resp.set_cookie("dressing", dressing)
        resp.set_cookie("onion", onion)
        resp.set_cookie("patty", patty)
        resp.set_cookie("pickles", pickles)
        return resp

    
    cheese = request.cookies.get("cheese", 1)
    dressing = request.cookies.get("dressing", 1)
    onion = request.cookies.get("onion", 3)
    patty = request.cookies.get("patty", 1)
    pickles = request.cookies.get("pickles", 3)


    return render_template("BurgerOrderer.html", cheese=cheese, dressing=dressing, onion=onion, patty=patty, pickles=pickles)

@app.route("/OrderConfirmation.html")
def order_confirmation(order_id):

    order = session.query(Order).get(order_id)

    return render_template("OrderConfirmation.html", order=order, order_id=order_id)

if __name__ == "__main__":
    app.run(debug=True)  
    