"""
Tests the code within the kitchenview.py file
"""

import pytest
from flask import Flask
from kitchenview import app  # assuming your Flask app is in app.py
from unittest.mock import patch

@pytest.fixture
def client():
    """
    Tells flask to use the current session to run tests on
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        """
        
        """
        yield client

def test_so_burger_exists(client):
    """
    Tests so that a burger has been created and that you can check if the order exsists
    """
    response = client.get('/')
    assert response.status_code == 404  # Ensure the page loads correctly
    
def test_so_order_confirmation(client):
    """
    Tests so that the order confirmation page works
    """
    response = client.get('/OrderConfirmation.html?order_id=1')
    assert response.status_code == 200  # Ensure the page loads correctly
    assert b"order_conformation" in response.data  # Ensure the page contains the order_id        
    assert b"Pickles" in response.data  # Ensure the page contains the Pickles
    assert b'>Order ID: None</p' not in response.data  # Ensure the page contains the order_id        
    
    assert b"Dressing" in response.data  # Ensure the page contains the Dressing

def test_non_working_post(client): 
    """
    Checks that if you go into the OrderConfirmation.html page without a order id there shouldn't be a burger there
    """ 
    response = client.get('/OrderConfirmation.html')
    assert b'>Order ID: None</p' in response.data  # Ensure the page contains the order_id        

    