<div align="center">

# 30 Days of Python Projects

**A progressive collection of 30 practical Python projects — from desktop utilities to APIs, automation, databases, and defensive security tooling.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Projects](https://img.shields.io/badge/Projects-30-0A66C2)](#project-roadmap)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Maintained by](https://img.shields.io/badge/Maintained%20by-DzarelDeveloper-181717?logo=github)](https://github.com/DzarelDeveloper)

[Explore the roadmap](#project-roadmap) · [Get started](#getting-started) · [View structure](#repository-structure)

</div>

---

## About This Repository

This repository documents a hands-on Python learning journey through 30 standalone projects. The roadmap starts with approachable desktop applications and gradually introduces file processing, authentication, external APIs, automation, databases, REST services, and defensive log analysis.

Each project lives in its own directory and includes:

- A standalone `main.py` entry point
- A short project-specific README
- Clear source attribution where the project originated from an earlier repository
- A difficulty level that reflects its concepts and dependencies

> **Project history:** Days 01–26 consolidate existing projects without modifying their original repositories. Days 27–30 are new capstone projects created for this collection.

## Learning Path

| Stage | Days | Focus |
|---|---:|---|
| **Beginner** | 01–10 | Python fundamentals, GUI basics, images, and small utilities |
| **Intermediate** | 11–20 | State, files, authentication, desktop tools, and network utilities |
| **Advanced** | 21–30 | Bots, APIs, speech processing, AI, SQLite, Flask, FastAPI, and security logs |

## Project Roadmap

<details open>
<summary><strong>Beginner — Days 01–10</strong></summary>

| Day | Project | Core Concepts |
|---:|---|---|
| 01 | [Calculator](./Day-01/) | Tkinter, functions, event handling |
| 02 | [QR Code Generator](./Day-02/) | Package usage, QR generation |
| 03 | [Birthday Message](./Day-03/) | Output formatting, control flow |
| 04 | [Personal Message Script](./Day-04/) | Strings, timing, terminal output |
| 05 | [Notepad](./Day-05/) | GUI, text editing |
| 06 | [Personal Diary](./Day-06/) | File handling, user input |
| 07 | [Image Converter](./Day-07/) | Image processing, file conversion |
| 08 | [Color Picker](./Day-08/) | GUI dialogs, color values |
| 09 | [Screenshot Tool](./Day-09/) | Desktop automation, image capture |
| 10 | [Image Watermark](./Day-10/) | Image composition, positioning |

</details>

<details open>
<summary><strong>Intermediate — Days 11–20</strong></summary>

| Day | Project | Core Concepts |
|---:|---|---|
| 11 | [Multi-Function Timer](./Day-11/) | Time management, application state |
| 12 | [Study Timer](./Day-12/) | Productivity logic, GUI state |
| 13 | [Smart Calendar](./Day-13/) | Dates, calendar UI |
| 14 | [Music Player](./Day-14/) | Audio playback, media controls |
| 15 | [File Manager](./Day-15/) | Filesystem operations, navigation |
| 16 | [Password Manager](./Day-16/) | Credential storage concepts |
| 17 | [Text Encrypt & Decrypt](./Day-17/) | Cryptography fundamentals |
| 18 | [Register & Login](./Day-18/) | Authentication flow, validation |
| 19 | [QR Scanner](./Day-19/) | Camera input, QR decoding |
| 20 | [Subdomain Hunter](./Day-20/) | Networking, HTTP requests |

</details>

<details open>
<summary><strong>Advanced — Days 21–30</strong></summary>

| Day | Project | Core Concepts |
|---:|---|---|
| 21 | [Telegram Bot](./Day-21/) | Bot APIs, message handlers |
| 22 | [ChatGPT Client](./Day-22/) | AI API integration |
| 23 | [Language Translator](./Day-23/) | Translation services, GUI |
| 24 | [Audio Transcription](./Day-24/) | Speech recognition, audio input |
| 25 | [Tic-Tac-Toe vs AI](./Day-25/) | Game logic, computer opponent |
| 26 | [Restaurant Management System](./Day-26/) | GUI, transactions, billing |
| 27 | [Expense Tracker with SQLite](./Day-27/) | SQL, persistence, CLI |
| 28 | [REST API with FastAPI](./Day-28/) | REST, validation, HTTP methods |
| 29 | [Security Log Analyzer](./Day-29/) | Regex, log parsing, defensive analysis |
| 30 | [Task Manager with Flask & SQLite](./Day-30/) | Full-stack basics, CRUD, database |

</details>

## Getting Started

### Prerequisites

- Python **3.10 or newer**
- Git
- A virtual environment is strongly recommended

### Installation

```bash
git clone https://github.com/DzarelDeveloper/PythonProject.git
cd PythonProject

python -m venv .venv
source .venv/bin/activate
```

On Windows, activate the environment with:

```powershell
.venv\Scripts\activate
```

Install the shared dependencies:

```bash
pip install -r requirements.txt
```

Then open a project and run it:

```bash
cd Day-01
python main.py
```

Some projects require only part of the shared dependency list. Check the project's README and imports before installation.

## Repository Structure

```text
PythonProject/
├── Day-01/
│   ├── main.py
│   └── README.md
├── Day-02/
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

- Never commit API keys, bot tokens, passwords, or `.env` files.
- Use environment variables for projects that connect to external services.
- Run network and security-related projects only against systems you own or are explicitly authorized to test.
- Day 29 is intended for defensive analysis of authorized local logs.
- Review older learning projects before using them in production; educational code may require additional validation, error handling, testing, and security hardening.

## Contributing

Suggestions, bug reports, documentation improvements, and pull requests are welcome. When contributing:

1. Keep each project self-contained.
2. Do not include credentials or personal data.
3. Explain new dependencies.
4. Preserve attribution for code originating from another repository.
5. Test the project before submitting a pull request.

## Author

Created and maintained by **Muhamad Dzarel Alghifari**.

- GitHub: [@DzarelDeveloper](https://github.com/DzarelDeveloper)
- Website: [dzarel.com](https://dzarel.com)

## License

This project is available under the [MIT License](./LICENSE).

---

<div align="center">

**Learn consistently. Build practically. Improve one project at a time.**

If this repository helps you, consider giving it a ⭐.

</div>
