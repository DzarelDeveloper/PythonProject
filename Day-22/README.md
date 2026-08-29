# Day 22 — ChatGPT API Client

| Property | Value |
|---|---|
| **Difficulty** | Advanced |
| **Interface** | CLI / API Client |
| **Core concepts** | HTTP requests, API headers, loading animation |
| **Dependencies** | requests, pyfiglet |

## Learning Goals

By completing this project, you should be able to:

- Explain how the program receives input, processes data, and produces output
- Identify the main functions, state, and external resources used by the application
- Run and debug the project independently
- Modify at least one behavior without breaking the original flow

## Concepts

- HTTP requests
- API headers
- loading animation
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

Required dependencies: **requests, pyfiglet**.

Install any missing third-party package before running the project. Standard-library modules do not need to be installed with `pip`.

## Run the Project

From the repository root:

```bash
cd Day-22
python main.py
```



## How the Program Works

1. Python imports the modules required by the project.
2. The program initializes its cli / api client and application state.
3. It receives input from a user, file, device, request, or external service.
4. The main logic validates and processes that input.
5. The result is displayed through the cli / api client, saved locally, or returned to a client.
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

Move the API key to an environment variable and handle HTTP failures.

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
