# Week 6 - Continuous Integration in Python

## Project Overview
This project demonstrates Continuous Integration (CI)
using a Python Student Marks Calculator.

## Features
- Calculates student average marks.
- Assigns grades.
- Validates student names and marks.
- Handles invalid input.

## Project Files
- student_marks.py - Main Python application.
- test_student_marks.py - Automated unit tests.
- requirements.txt - Dependency information.
- .github/workflows/ci.yml - GitHub Actions workflow.

## How to Run
Run the application:

python student_marks.py

## How to Run Tests
Run:

python -m unittest -v

## Continuous Integration
GitHub Actions automatically runs the
automated tests when code is pushed to main
or when a pull request targets main.

## Test Results
All 10 automated unit tests passed locally.

## Tools Used
- Python 3.13
- Python unittest
- GitHub
- GitHub Actions
