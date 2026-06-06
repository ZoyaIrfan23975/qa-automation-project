# QA Automation Tests - Zoya Irfan
# Pytest test cases demonstrating automated testing

import requests

# Test 1 - Real API status code check
def test_real_api_returns_200():
  response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
  assert response.status_code == 200

# Test 2 - Check JSON response contains correct data
def test_api_response_contains_correct_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    assert data["id"] == 1
    assert "title" in data

# Test 3 - Login validation
def test_invalid_login_rejected():
    def login(username, password):
        if username == "" or password == "":
            return False
        if len(password) < 8:
            return False
        return True

    assert login("", "password123") == False
    assert login("zoya", "short") == False
    assert login("zoya", "validpass123") == True
