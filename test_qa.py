# QA Automation Tests - Zoya Irfan
# Pytest test cases demonstrating automated testing

import requets

# Test 1 - Real API status code check
def test_real_api_returns_200():
  response = request.get("https://jsonplaceholder.typicode.com/posts/1")
  assert response.status_code == 200

# Test 2 - Password length validation
# Simulates checking that a password meets minimum length requirements
def test_password_length(): 
  password = "securepass123"
  assert len(password) >= 8

# Test 3 - API status code validation
# Simulates checking that an API returns the expected status code
def test_api_status_code():
  expected_status = 200
  actual_status = 200
  assert actual_status == expected_status
  
