from flask import Flask, render_template, session, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
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
    return render_template("MenuStore.html")

def order_post():
    print(request.form)
    return request.form

@app.route("/BurgerOrderer.html", methods=["GET", "POST"])
def order():
    if request.method == "POST":

        cheese = request.form.get("cheese")
        dressing = request.form.get("dressing")
        onion = request.form.get("onion")
        patty = request.form.get("patty")
        pickles = request.form.get("pickles")

        order = Order(cheese, dressing, onion, patty, pickles)
        session.add(order)
        session.commit()
        return order_post()
    return render_template("BurgerOrderer.html")

if __name__ == "__main__":
    app.run(debug=True)  
    