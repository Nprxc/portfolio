"""Basic API tests."""

import os
import sys

# Allow imports from project root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask_endpoint():
    """Ensure /ask returns a JSON response with 'response' and history."""
    response = client.post('/ask', data={'question': 'test'})
    assert response.status_code == 200
    json_data = response.json()
    assert 'response' in json_data
    assert 'history' in json_data
    assert isinstance(json_data['history'], list)
    assert json_data['history'][-2]['role'] == 'user'
    assert json_data['history'][-2]['text'] == 'test'
    assert json_data['history'][-1]['role'] == 'assistant'
    assert json_data['history'][-1]['text'] == json_data['response']


def test_history_persistence():
    """Ensure chat history grows with each request."""
    first_len = len(client.post('/ask', data={'question': 'hello'}).json()['history'])
    second_len = len(client.post('/ask', data={'question': 'again'}).json()['history'])
    assert second_len == first_len + 2
