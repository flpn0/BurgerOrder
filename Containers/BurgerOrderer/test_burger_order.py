"""
Tests the code within burger_order.py
"""

import pytest
from flask import Flask
from burger_order import app 
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

@pytest.fixture
def client():
    """
    Tells flask to use the current session to run tests on
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_felix_fasande_hamburgare_exists(client):
    """
    Test if 'Felix Fasande Hamburgare' exists in the StartMenu.html page
    """
    response = client.get('/')
    assert response.status_code == 200  # Ensures that the page loads correctly
    assert b"Felix Fasande Hamburgare" in response.data  # Checks for the specific text
    
    
def test_burger_order(client):
    """
    Tests that the post and get functions of the BurgerOrderer.html page works correctly
    """
    response = client.get('/BurgerOrderer.html')
    assert response.status_code == 200  # Ensures the page loads correctly
    assert b"Rabatter" in response.data  # Checks for the specific text
    
    # Tests to send a POST request
    post_data = {
      "cheese": 1,
      "dressing":2,
      "onion": 3,
      "patty":4,
      "pickles":5
    }
    
    response = client.post('/BurgerOrderer.html?burger=flygande_faran', data=post_data)
    # Check if the response is a redirect to the OrderConfirmation.html page (302 is a redirect code, so if it gets redirected correctly it shoul return 302)
    print(response)
    assert response.status_code == 302
    
     