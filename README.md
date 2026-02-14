# Lab 1 - Automated Testing with GitHub Actions

**Author:** Nikhil Yellapragada  
**Student ID:** 002567331  
**Course:** Data Analytics Engineering  
**University:** Northeastern University  
**Semester:** Spring 2026  
**GitHub:** https://github.com/Nikhil20012/MLOps

---

## Project Overview

This lab implements automated testing for a Python calculator module using pytest and unittest frameworks. GitHub Actions runs these tests automatically whenever code is pushed to the repository, ensuring code quality and catching bugs before they reach production.

---

## Technologies Used

- Python 3.8
- pytest for testing
- unittest for testing
- GitHub Actions for CI/CD automation
- Git for version control

---

## My Modifications

**Calculator Functions**
- Renamed functions from fun1, fun2, fun3, fun4 to add, subtract, multiply, add_three for better clarity
- Added three new functions: divide, power, and square_root
- Implemented divide by zero error handling in the divide function
- Added negative number validation for square_root function
- Improved input validation across all functions

**Pytest Tests**
- Renamed test functions to match new calculator function names
- Added comprehensive test for divide function with multiple test cases
- Created test_divide_by_zero to verify ZeroDivisionError handling
- Added test_power with multiple scenarios including negative exponents
- Implemented test_square_root with approximate value testing
- Added test_square_root_negative to verify ValueError for negative inputs
- Improved path setup for better module imports

**Unittest Tests**
- Updated all test method names to match new calculator functions
- Added test_divide with comprehensive test cases
- Implemented test_divide_by_zero using assertRaises context manager
- Added test_power with multiple scenarios
- Created test_square_root using assertAlmostEqual for floating point comparison
- Added test_square_root_negative for error handling verification
- Enhanced path configuration for reliable imports

**GitHub Actions Workflows**
- Simplified pytest_action.yml by removing unnecessary triggers (branches-ignore, label, issues)
- Updated action versions from v2 to v4 and v5 for better compatibility
- Cleaned up workflow triggers to only run on push to main branch
- Simplified unittest_action.yml with updated action versions
- Removed complex branching logic for cleaner CI/CD pipeline
- Standardized step naming with proper capitalization

---

## Prerequisites

- Python 3.8 or higher
- Git installed
- GitHub account
- Basic understanding of Python and testing

---

## Setup Instructions

**Step 1: Clone the Repository**
```bash
git clone https://github.com/Nikhil20012/MLOps.git
cd MLOps/Labs/Lab_1
```

**Step 2: Create Virtual Environment**

For Mac/Linux:
```bash
python -m venv lab_01
source lab_01/bin/activate
```

For Windows:
```bash
python -m venv lab_01
lab_01\Scripts\activate
```

**Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

**Step 4: Run Tests Locally**

Run pytest tests:
```bash
pytest test/test_pytest.py
```

Run unittest tests:
```bash
python -m unittest test.test_unittest
```

---

## Project Structure
```
Lab_1/
├── .github/
│   └── workflows/
│       ├── pytest_action.yml
│       └── unittest_action.yml
├── src/
│   └── calculator.py
├── test/
│   ├── test_pytest.py
│   └── test_unittest.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Calculator Functions

**add(x, y)** - Adds two numbers

**subtract(x, y)** - Subtracts y from x

**multiply(x, y)** - Multiplies two numbers

**add_three(x, y, z)** - Adds three numbers together

**divide(x, y)** - Divides x by y with zero division error handling

**power(x, y)** - Raises x to the power of y

**square_root(x)** - Calculates square root with negative number validation

---

## Testing

**Pytest Tests**

The pytest test suite includes 9 test functions covering all calculator operations including edge cases like division by zero and negative square roots.

Run with:
```bash
pytest test/test_pytest.py -v
```

**Unittest Tests**

The unittest test suite uses the TestCase class with 9 test methods covering the same scenarios as pytest.

Run with:
```bash
python -m unittest test.test_unittest -v
```

---

## GitHub Actions

Two automated workflows run on every push to the main branch:

**pytest_action.yml**
- Checks out code
- Sets up Python 3.8
- Installs dependencies
- Runs pytest with XML report generation
- Uploads test results as artifacts
- Notifies on success or failure

**unittest_action.yml**
- Checks out code
- Sets up Python 3.8
- Installs dependencies
- Runs unittest test suite
- Notifies on success or failure

---

## How to View Test Results

After pushing code to GitHub:

1. Go to your repository on GitHub
2. Click the "Actions" tab
3. Select the workflow run you want to view
4. Check the test results and logs

---

## Troubleshooting

**Tests failing locally**

Make sure your virtual environment is activated and all dependencies are installed from requirements.txt.

**Import errors**

Check that the path setup in test files correctly points to the project root directory.

**GitHub Actions not running**

Verify that the workflow files are in the .github/workflows directory and that you pushed to the main branch.

**Action version errors**

Make sure you're using updated action versions (v4 for checkout and upload-artifact, v5 for setup-python).

---

## Files Modified

- calculator.py - Renamed functions, added divide, power, square_root functions
- test_pytest.py - Updated test names, added 5 new test functions
- test_unittest.py - Updated test methods, added 5 new test methods
- pytest_action.yml - Simplified triggers, updated action versions
- unittest_action.yml - Updated action versions, cleaned up workflow
- README.md - Written from scratch

---
