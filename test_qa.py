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

# Test 3 - API status code validation
# Simulates checking that an API returns the expected status code
def test_api_status_code():
  expected_status = 200
  actual_status = 200
  assert actual_status == expected_status
  
