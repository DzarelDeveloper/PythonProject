<div align="center">

# 30 Days of Python Projects

**A progressive, project-based Python learning path—from fundamental desktop utilities to APIs, databases, automation, and defensive security tools.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Projects](https://img.shields.io/badge/Projects-30-0A66C2)](#project-roadmap)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Maintainer](https://img.shields.io/badge/Maintainer-DzarelDeveloper-181717?logo=github)](https://github.com/DzarelDeveloper)

[Project roadmap](#project-roadmap) · [Getting started](#getting-started) · [Learning workflow](#recommended-learning-workflow)

</div>

---

## Overview

**30 Days of Python Projects** is a hands-on learning program containing one practical project for each day. The collection gradually introduces Python fundamentals, graphical applications, file processing, network requests, third-party APIs, data persistence, web development, and defensive log analysis.

Every day includes a focused tutorial with learning goals, setup instructions, a program-flow explanation, guided experiments, an extension challenge, and a completion checklist.

## Learning Stages

| Stage | Days | Main Focus |
|---|---:|---|
| **Beginner** | 01–10 | Python fundamentals, functions, GUI basics, files, and images |
| **Intermediate** | 11–20 | Application state, persistence, audio, authentication, and networking |
| **Advanced** | 21–30 | Bots, external APIs, databases, REST services, web apps, and security logs |

## Interface Guide

| Interface | Meaning |
|---|---|
| **CLI** | Runs and accepts input in a terminal |
| **Desktop GUI** | Opens a desktop window, mainly using Tkinter |
| **Graphics Window** | Opens a drawing or animation canvas |
| **Chat Bot** | Interacts through a messaging platform |
| **REST API** | Exposes HTTP endpoints for another client |
| **Web App** | Runs a browser-based user interface |
| **API Client** | Connects to an external service |
| **Security Tool** | Intended for authorized defensive or educational use |

## Project Roadmap

| Day | Project | Level | Interface | Core Concepts |
|---:|---|---|---|---|
| 01 | [Calculator](./Day-01/) | Beginner | **Desktop GUI** | Tkinter, functions, event handling |
| 02 | [QR Code Generator](./Day-02/) | Beginner | **CLI / File Output** | QR encoding, package usage, image output |
| 03 | [Birthday Turtle Animation](./Day-03/) | Beginner | **Graphics Window** | Turtle graphics, coordinates, animation |
| 04 | [Personal Message Animation](./Day-04/) | Beginner | **CLI** | Strings, terminal styling, timing |
| 05 | [Notepad](./Day-05/) | Beginner | **Desktop GUI** | Tkinter Text widget, save dialog, file writing |
| 06 | [Personal Diary](./Day-06/) | Beginner | **Desktop GUI** | Text input, timestamps, append-mode files |
| 07 | [Image Converter](./Day-07/) | Beginner | **Desktop GUI** | File dialogs, Pillow, image conversion |
| 08 | [Color Picker](./Day-08/) | Beginner | **Desktop GUI** | Color dialog, HEX/RGB, contrast |
| 09 | [Screenshot Tool](./Day-09/) | Beginner | **Desktop GUI** | Screen capture, canvas, image annotation |
| 10 | [Image Watermark](./Day-10/) | Beginner | **Desktop GUI** | Pillow, text positioning, image export |
| 11 | [Multi-Function Timer](./Day-11/) | Intermediate | **Desktop GUI** | Countdown state, threading, time |
| 12 | [Study Timer](./Day-12/) | Intermediate | **Desktop GUI** | Study/break cycles, application state |
| 13 | [Smart Calendar](./Day-13/) | Intermediate | **Desktop GUI** | Dates, JSON persistence, calendar widgets |
| 14 | [Music Player](./Day-14/) | Intermediate | **Desktop GUI** | Audio playback, controls, file selection |
| 15 | [File Manager](./Day-15/) | Intermediate | **Desktop GUI** | Filesystem navigation, rename, delete |
| 16 | [Password Manager](./Day-16/) | Intermediate | **Desktop GUI** | JSON persistence, password generation |
| 17 | [Text Encrypt & Decrypt](./Day-17/) | Intermediate | **Desktop GUI** | Caesar cipher, character encoding, validation |
| 18 | [Register & Login](./Day-18/) | Intermediate | **Desktop GUI** | Registration flow, file persistence, validation |
| 19 | [Terminal QR Code Generator](./Day-19/) | Intermediate | **CLI** | Terminal UI, QR rendering, input loop |
| 20 | [Subdomain Hunter](./Day-20/) | Intermediate | **CLI / Network Tool** | HTTP requests, parsing, wordlists |
| 21 | [Telegram AI Bot](./Day-21/) | Advanced | **Chat Bot** | Telegram handlers, AI responses, logging |
| 22 | [ChatGPT API Client](./Day-22/) | Advanced | **CLI / API Client** | HTTP requests, API headers, loading animation |
| 23 | [Language Translator](./Day-23/) | Advanced | **Desktop GUI / API Client** | Translation service, language selection, GUI |
| 24 | [Audio Transcription](./Day-24/) | Advanced | **Desktop GUI** | Microphone input, speech recognition, errors |
| 25 | [Tic-Tac-Toe vs AI](./Day-25/) | Advanced | **Desktop GUI / Game** | Game state, random AI, difficulty settings |
| 26 | [Restaurant Management System](./Day-26/) | Advanced | **Desktop GUI** | Orders, totals, tax, invoice logic |
| 27 | [Expense Tracker with SQLite](./Day-27/) | Advanced | **CLI / Database** | argparse, SQLite, SQL aggregation |
| 28 | [Task REST API](./Day-28/) | Advanced | **REST API** | FastAPI, Pydantic, CRUD, HTTP methods |
| 29 | [Security Log Analyzer](./Day-29/) | Advanced | **CLI / Security Tool** | Regex, log parsing, counters, thresholds |
| 30 | [Task Manager with Flask & SQLite](./Day-30/) | Advanced | **Web App / Database** | Flask routes, forms, CRUD, SQLite |

## Getting Started

### Prerequisites

- Python 3.10 or newer
- Git
- A code editor such as Visual Studio Code
- Basic terminal knowledge

### Clone and prepare the environment

```bash
git clone https://github.com/DzarelDeveloper/PythonProject.git
cd PythonProject
python -m venv .venv
```

Activate the virtual environment:

```bash
# Linux or macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install the shared dependencies:

```bash
pip install -r requirements.txt
```

Start with Day 01:

```bash
cd Day-01
python main.py
```

Read the README inside each day's directory before running its program. Some projects require a desktop environment, microphone, internet connection, bot token, or API credential.

## Recommended Learning Workflow

1. Read the learning goals and concepts for the day.
2. Run the original program and observe its behavior.
3. Read `main.py` from the imports to the entry point.
4. Identify the input, processing logic, state, and output.
5. Perform the guided experiments.
6. Test at least one invalid or unexpected input.
7. Complete the extension challenge before moving forward.
8. Record what failed, why it failed, and how you fixed it.

## Repository Structure

```text
PythonProject/
├── Day-01/
│   ├── main.py
│   └── README.md
├── ...
├── Day-30/
│   ├── main.py
│   └── README.md
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Security and Responsible Use

- Never commit passwords, API keys, bot tokens, or `.env` files.
- Store credentials in environment variables.
- Run network-related projects only against systems you own or have explicit permission to test.
- Analyze only logs you are authorized to access.
- Review validation, error handling, tests, and security before using educational code in production.

## Contributing

Issues and pull requests are welcome. Keep projects easy to study, document new dependencies, exclude sensitive data, and test all changes.

## Author

Created and maintained by **Muhamad Dzarel Alghifari**.

- GitHub: [@DzarelDeveloper](https://github.com/DzarelDeveloper)
- Website: [dzarel.com](https://dzarel.com)

## License

Licensed under the [MIT License](./LICENSE).

---

<div align="center">

**Learn consistently. Build practically. Improve one project every day.**

</div>
