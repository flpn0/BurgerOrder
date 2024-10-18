"""
Tests the database
"""

from BurgerOrderer.burger_order import Order
from flask import Flask, render_template, session, request, redirect
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import pytest

def connect_to_db():
    """
    Initialieses a connection to the database and test so that the connection is valid
    """
    Base = declarative_base()
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///mydb.db') #Specifies what database we want to use for this
    engine = create_engine(DATABASE_URL, echo=True) #This runs create table SQL commands
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    assert engine.echo == True, "Should be True"
    assert session == session, "Should be session"
    
    return session

def test_order():
    """
    Performes test on the order model to check if the types and inputs are valid
    """

    # runs an assert that should fail because patty is a string
    cheese = 1
    dressing = 1
    onion = 2
    patty = "1"
    pickles = 1
    order = Order(cheese, dressing, onion, patty, pickles)

    # runs some basic tests on the ingredients
    assert order.cheese == 1, "Should be 1"
    assert order.dressing == 1, "Should be 1"
    assert order.onion != 1, "Should not be 1"
    assert type(order.patty) != int, "Should be int"

    # All these values should be numberts
    assert type(order.cheese) == int, "Should be int"
    assert type(order.dressing) == int, "Should be int"
    assert type(order.onion) == int, "Should be int"
    assert type(order.pickles) == int, "Should be int"
    
    order.patty = 1
    
    assert order.patty == 1 and type(order.patty) == int, "Should be 1"
    
    # If the order is missing a argument
    try:
        order = Order(cheese, dressing, onion, patty)
    except TypeError:
        pass
    else:
        assert False, "Should raise TypeError"

def test_db():
    """
    Tests different database querys to check if the data is valid
    """
    db_session = connect_to_db()
    # Removes all the orders from the database
    db_session.query(Order).delete()
    
    # Checks so that there are no orders in the database
    orders = db_session.query(Order).all()
    assert len(orders) == 0, "Should be 0"
  
    cheese = 1
    dressing = 1
    onion = 2
    patty = 1
    pickles = 1
    
    # Adds an order again
    order_1 = Order(cheese, dressing, onion, patty, pickles)
    db_session.add(order_1)
    db_session.commit()
    
    # Checks if the order is in the database
    order = db_session.query(Order).first()
    assert order == order, "Should be order"
    
    # Checks if the order is in the database again
    order = db_session.query(Order).first()
    assert order.cheese == 1, "Should be 1"
    assert order.dressing == 1, "Should be 1"
    assert order.onion == 2, "Should be 2"
    assert order.patty == 1, "Should be 1"
    assert order.pickles == 1, "Should be 1"

    # Creates a new entry in the database
    cheese = 2
    dressing = 2
    onion = 3
    patty = 2
    pickles = 2
    order_2 = Order(cheese, dressing, onion, patty, pickles)
    db_session.add(order_2)
    db_session.commit()
    
    # Checks how many entries there are in the database
    orders = db_session.query(Order).all()
    print(orders)
    assert len(orders) == 2, "Should be 2"
    
    # Selects burger 2 and check if the values are correct and valid
    order = db_session.get(Order, order_2.id)
    assert order.cheese == 2, "Should be 2"
