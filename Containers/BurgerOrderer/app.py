from flask import Flask, render_template, session, request, redirect
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
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
        This makes a constructor theat should make every row faster and easier to read
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
      
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///mydb.db') #Specifies what database we want to use for this
engine = create_engine(DATABASE_URL, echo=True) #This runs create table SQL commands
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

@app.route("/")
def home():
    """
    This renders the Home Page of the website, the first page, where you choose what burger you want.
    """
    return render_template("StartMenu.html")

def order_post():
    """
    Old testing 
    """
    print(request.form)
    return request.form

@app.route("/BurgerOrderer.html", methods=["GET", "POST"])
def MenuStore():
    """
    This is where we the data, that gets sent from the server after the user has chosen their ingridients and pressed submit, gets added to the database. If the request is a POST
    """

    if request.method == "POST": 
        
        # Gets the information from the server with a post request and defines what the ingridients are
        burger = request.args.get("burger")
        cheese = request.form.get("cheese")
        dressing = request.form.get("dressing")
        onion = request.form.get("onion")
        patty = request.form.get("patty")
        pickles = request.form.get("pickles")

        # If the request was a POST 
        order = Order(cheese, dressing, onion, patty, pickles)
        session.add(order)
        session.commit()
        
        # Redirects to burger after the POST request is processed. It takes the burger that was chosen and redirects it to the next port, to display what ingridients was chosen with it
        return redirect("http://localhost:5000/OrderConfirmation.html?order_id=" + str(order.id) + "&burger=" + str(burger) )

    # This uses cookies to remember the users last changes in the ingridients list if the user backs out from where you decide ingridients and then goes back in again
    cheese = request.cookies.get("cheese", 1)
    dressing = request.cookies.get("dressing", 1)
    onion = request.cookies.get("onion", 3)
    patty = request.cookies.get("patty", 1)
    pickles = request.cookies.get("pickles", 3)

    return render_template("BurgerOrderer.html", cheese=cheese, dressing=dressing, onion=onion, patty=patty, pickles=pickles)

if __name__ == "__main__":
    app.run(debug=True, port=8000, host="0.0.0.0")