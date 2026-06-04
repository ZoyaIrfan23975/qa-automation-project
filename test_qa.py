# QA Automation Tests - Zoya Irfan
# Pytest test cases demonstrating automated testing

# Test 1 - Basic validation check
def test_basic_check(): 
  assert 1 + 1 == 2

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
  assert actual_status = expected_status
  
