# QA Automation Project

A practical test automation suite built to demonstrate real-world QA engineering skills, including API testing, functional validation, and data integrity checks — all running automatically through a CI/CD pipeline using GitHub Actions.

---

## About This Project

This project was built to showcase hands-on experience in test automation as part of a professional QA engineering portfolio. It reflects the kind of testing activities carried out daily in Agile software delivery teams — validating API responses, checking data integrity, and ensuring application logic behaves correctly.

All tests run automatically every time a change is pushed to the repository, demonstrating a working CI/CD pipeline with zero manual intervention required.

---

## Technologies Used

- **Python** — primary scripting language
- **Pytest** — test automation framework
- **Requests** — Python library for REST API testing
- **GitHub Actions** — CI/CD pipeline for automated test execution

---

## Test Cases

### Test 1 — API Status Code Validation
Calls a live REST API endpoint and validates that it returns HTTP status code 200 (OK).
Reflects real-world API testing experience using tools like Postman.

### Test 2 — JSON Response Data Validation
Calls a live REST API and validates that the JSON response contains the correct data fields and values.
Reflects experience in verifying response body structure and data integrity.

### Test 3 — Login Functional Validation
Validates that a login function correctly rejects invalid credentials — including empty usernames, empty passwords, and passwords that are too short — while accepting valid credentials.
Reflects functional testing of user authentication flows.

### Test 4 — Data Format and Integrity Validation
Calls a live REST API that returns a list of records and validates that the response is the correct format, is not empty, and contains the expected fields.
Reflects experience in data integrity testing and response format validation.

---

## CI/CD Pipeline

Every time code is pushed to this repository, GitHub Actions automatically:

1. Sets up a Python environment
2. Installs all dependencies
3. Runs all four test cases
4. Reports pass or fail results

This ensures continuous testing with fast feedback — a core principle of modern Agile software delivery.

---



## Author

**Zoya Irfan** — QA Engineer with 3+ years experience in manual and automated testing across SaaS and enterprise software environments.

[LinkedIn Profile](https://www.linkedin.com/in/zoya-irfan-513a61235/)

## Test Results

All four tests currently passing:
