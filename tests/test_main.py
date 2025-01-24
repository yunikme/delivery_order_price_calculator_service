import pytest
from main import dopc
from flask import json 

@pytest.fixture
def client():
    dopc.config['TESTING'] = True 
    with dopc.test_client() as client:
        yield client
