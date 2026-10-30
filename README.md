# Week 6 - Continuous Integration Project

## Project Overview
This project demonstrates Continuous Integration (CI) using GitHub Actions for a Python Student Marks Calculator.

The application calculates the average marks, assigns grades, and generates student reports. Unit tests are used to verify the functionality, and Ruff checks code quality.

## Project Structure

```text
Week6-CI-Project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── student_marks.py
├── test_student_marks.py
├── requirements.txt
├── .gitignore
├── ci_testing_log.txt
├── Week6_CI_Report.docx
└── README.md
```

## Requirements
- Python 3.10 or later
- Ruff

## How to Run the Project

Open a terminal in the project folder and run:

```bash
python student_marks.py
```

## How to Run Unit Tests

Run:

```bash
python -m unittest -v
```

The project contains 10 unit tests covering average calculation, grade assignment, input validation, and report generation.

## Code Quality Check

Install Ruff:

```bash
python -m pip install ruff
```

Run the code quality check:

```bash
ruff check student_marks.py test_student_marks.py
```

## Continuous Integration

GitHub Actions automatically runs the following checks when code is pushed to the `main` branch or a pull request targets `main`:

1. Checks out the repository.
2. Sets up Python.
3. Installs Ruff.
4. Checks code quality.
5. Runs automated unit tests.

## Testing Results

- Automated unit tests: Passed locally (10 tests).
- Ruff code quality check: Passed locally.
- GitHub Actions: Latest workflow run succeeded.

## Conclusion

This project demonstrates automated testing and code quality checks using GitHub Actions to support reliable Python development.
