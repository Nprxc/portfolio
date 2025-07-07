"""Basic API tests."""

import os
import sys

# Allow imports from project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask_endpoint():
    """Ensure /ask returns a JSON response with 'response' key."""
    response = client.post('/ask', data={'question': 'test'})
    assert response.status_code == 200
    json_data = response.json()
    assert 'response' in json_data
