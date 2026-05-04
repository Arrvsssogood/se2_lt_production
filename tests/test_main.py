import pytest
# This reaches into the 'app' folder and grabs your 'app' object
from app.main import app 

def test_index_status():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200 # Ensures the page loads

def test_pick_endpoint():
    client = app.test_client()
    res = client.get('/pick')
    assert res.status_code == 200
    assert b"food" in res.data # Ensures JSON is working