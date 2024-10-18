"""
Kitchen view API code
"""

from flask import Flask, render_template, session, request
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()
app = Flask(__name__, template_folder='templates')

class Order(Base):
    """
    Here we setup the database Colums
    """
    __tablename__ = "orders"

    id = Column("id", Integer, primary_key=True)
    cheese = Column("cheese", Integer)
    dressing = Column("dressing", Integer)
    onion = Column("onion", Integer)
    patty = Column("patty", Integer)
    pickles = Column("pickles", Integer)

    def __init__(self, cheese, dressing, onion, patty, pickles):
        """
        This makes a constructor that should make every row faster and easier to read
        """

        self.cheese = cheese
        self.dressing = dressing
        self.onion = onion
        self.patty = patty
        self.pickles = pickles

    def __repr__(self):
        """
        This makes the printing of the order easier, however im not too sure when we has ever used this
        """
        personal_order = f"{self.cheese}, {self.dressing}, {self.onion}, {self.patty}, {self.pickles}"
        return personal_order
      
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///mydb.db') # Specifies what database we want to use for this
engine = create_engine(DATABASE_URL, echo=True) # This runs create table SQL commands
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

@app.route("/OrderConfirmation.html")
def order_confirmation():
    """
    This gets the user order ingridients and the order_id to print, then it prints it on the OrderConfirmation site so the user know what they ordered and what order id they have
    """
    order_id = request.args.get("order_id")
    order = None
    if order_id:
        order = session.get(Order, order_id)
    return render_template("OrderConfirmation.html", order=order, order_id=order_id)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")  
    