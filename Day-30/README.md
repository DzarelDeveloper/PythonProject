# Day 30 — Task Manager with Flask & SQLite

| Property | Value |
|---|---|
| **Difficulty** | Advanced |
| **Interface** | Web App / Database |
| **Core concepts** | Flask routes, forms, CRUD, SQLite |
| **Dependencies** | Flask |

## Learning Goals

By completing this project, you should be able to:

- Explain how the program receives input, processes data, and produces output
- Identify the main functions, state, and external resources used by the application
- Run and debug the project independently
- Modify at least one behavior without breaking the original flow

## Concepts

- Flask routes
- forms
- CRUD
- SQLite
- Input validation and error handling
- Breaking a problem into smaller functions or components

## Setup

Create and activate a virtual environment:

```bash
python -m venv .venv

# Linux or macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Required dependencies: **Flask**.

Install any missing third-party package before running the project. Standard-library modules do not need to be installed with `pip`.

## Run the Project

From the repository root:

```bash
cd Day-30
python main.py
```

Then open `http://127.0.0.1:5000` in a browser.

## How the Program Works

1. Python imports the modules required by the project.
2. The program initializes its web app / database and application state.
3. It receives input from a user, file, device, request, or external service.
4. The main logic validates and processes that input.
5. The result is displayed through the web app / database, saved locally, or returned to a client.
6. Errors should be converted into clear feedback instead of terminating the program unexpectedly.

Open `main.py` and trace the program from its imports to its entry point. Locate the code responsible for input, business logic, state changes, and output.

## Guided Practice

- Run the unmodified project and record the expected result.
- Change one label, default value, or configuration.
- Test one valid input and one invalid input.
- Add a temporary `print()` statement to inspect a value.
- Remove temporary debugging output after understanding the flow.
- Explain the project in your own words without reading the code.

## Extension Challenge

Add authentication, CSRF protection, styling, and automated tests.

## Completion Checklist

- [ ] The project runs successfully
- [ ] I can identify its interface type
- [ ] I understand its input, processing, and output
- [ ] I can explain the main function or class
- [ ] I tested an invalid input or failure case
- [ ] I completed at least one modification
- [ ] No credentials or sensitive data are committed

## Production Note

This is a learning project. Review its validation, security, error handling, dependency versions, and test coverage before using it in a real environment.
