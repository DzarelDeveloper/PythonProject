<div align="center">

# 30 Days of Python Projects

**Belajar Python melalui 30 proyek praktis yang disusun bertahap dari tingkat pemula hingga lanjutan.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Projects](https://img.shields.io/badge/Projects-30-0A66C2)](#roadmap-proyek)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE)
[![Maintainer](https://img.shields.io/badge/Maintainer-DzarelDeveloper-181717?logo=github)](https://github.com/DzarelDeveloper)

[Roadmap](#roadmap-proyek) · [Mulai belajar](#cara-memulai) · [Struktur](#struktur-repository)

</div>

---

## Tentang Program

**30 Days of Python Projects** adalah jalur belajar berbasis praktik. Setiap hari membahas satu proyek dengan sasaran yang jelas, konsep utama, petunjuk menjalankan program, penjelasan alur, latihan, dan tantangan pengembangan.

Program ini bergerak dari fundamental Python dan aplikasi desktop menuju pengolahan file, API, database, otomasi, pengembangan web, serta analisis log keamanan defensif.

## Tahapan Belajar

| Tahap | Hari | Fokus |
|---|---:|---|
| **Pemula** | 01–10 | Fundamental Python, fungsi, GUI, input, file, dan gambar |
| **Menengah** | 11–20 | State aplikasi, autentikasi, audio, filesystem, dan networking |
| **Lanjutan** | 21–30 | Bot, AI API, database, REST API, web app, dan defensive security |

## Roadmap Proyek

| Hari | Proyek | Level | Konsep Utama |
|---:|---|---|---|
| 01 | [Calculator](./Day-01/) | Pemula | Tkinter, fungsi, event handling |
| 02 | [QR Code Generator](./Day-02/) | Pemula | input pengguna, library pihak ketiga, penyimpanan file |
| 03 | [Birthday Message](./Day-03/) | Pemula | string, output terminal, jeda waktu |
| 04 | [Personal Message Script](./Day-04/) | Pemula | string, perulangan, timing |
| 05 | [Notepad](./Day-05/) | Pemula | Tkinter, widget Text, operasi file |
| 06 | [Personal Diary](./Day-06/) | Pemula | input, file handling, tanggal |
| 07 | [Image Converter](./Day-07/) | Pemula | dialog file, format gambar, Pillow |
| 08 | [Color Picker](./Day-08/) | Pemula | dialog warna, HEX, RGB |
| 09 | [Screenshot Tool](./Day-09/) | Pemula | desktop capture, penyimpanan gambar |
| 10 | [Image Watermark](./Day-10/) | Pemula | Pillow, koordinat, transparansi |
| 11 | [Multi-Function Timer](./Day-11/) | Menengah | state aplikasi, waktu, callback |
| 12 | [Study Timer](./Day-12/) | Menengah | Pomodoro, state, validasi input |
| 13 | [Smart Calendar](./Day-13/) | Menengah | tanggal, kalender GUI, event |
| 14 | [Music Player](./Day-14/) | Menengah | audio playback, playlist, event GUI |
| 15 | [File Manager](./Day-15/) | Menengah | path, folder, operasi filesystem |
| 16 | [Password Manager](./Day-16/) | Menengah | penyimpanan data, validasi, keamanan dasar |
| 17 | [Text Encrypt & Decrypt](./Day-17/) | Menengah | kriptografi simetris, key, encoding |
| 18 | [Register & Login](./Day-18/) | Menengah | autentikasi, validasi, hashing |
| 19 | [QR Scanner](./Day-19/) | Menengah | kamera, decoding QR, loop frame |
| 20 | [Subdomain Hunter](./Day-20/) | Menengah | DNS/HTTP, wordlist, request, error handling |
| 21 | [Telegram Bot](./Day-21/) | Lanjutan | Bot API, handler, token lingkungan |
| 22 | [ChatGPT Client](./Day-22/) | Lanjutan | API, environment variable, respons model |
| 23 | [Language Translator](./Day-23/) | Lanjutan | translation API, bahasa sumber/tujuan, GUI |
| 24 | [Audio Transcription](./Day-24/) | Lanjutan | audio input, speech recognition, error handling |
| 25 | [Tic-Tac-Toe vs AI](./Day-25/) | Lanjutan | game state, pencarian langkah, strategi AI |
| 26 | [Restaurant Management System](./Day-26/) | Lanjutan | GUI, item pesanan, total, invoice |
| 27 | [Expense Tracker with SQLite](./Day-27/) | Lanjutan | SQLite, SQL, argparse, agregasi |
| 28 | [REST API with FastAPI](./Day-28/) | Lanjutan | REST, HTTP methods, Pydantic, validation |
| 29 | [Security Log Analyzer](./Day-29/) | Lanjutan | regex, parsing log, Counter, CLI |
| 30 | [Task Manager with Flask & SQLite](./Day-30/) | Lanjutan | Flask, routing, template, CRUD, SQLite |

## Cara Memulai

### Prasyarat

- Python 3.10 atau lebih baru
- Git
- Editor kode seperti Visual Studio Code
- Dasar penggunaan terminal

### Instalasi

```bash
git clone https://github.com/DzarelDeveloper/PythonProject.git
cd PythonProject
python -m venv .venv
```

Aktifkan virtual environment:

```bash
# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Instal dependensi bersama:

```bash
pip install -r requirements.txt
```

Mulai dari hari pertama:

```bash
cd Day-01
python main.py
```

Baca `README.md` di dalam folder setiap hari sebelum menjalankan program.

## Cara Belajar yang Disarankan

1. Baca tujuan dan konsep pada README hari tersebut.
2. Jalankan program tanpa mengubah kode untuk memahami perilakunya.
3. Baca `main.py` dari atas ke bawah.
4. Ubah satu bagian kecil dan amati hasilnya.
5. Kerjakan latihan mandiri.
6. Selesaikan tantangan sebelum berpindah ke hari berikutnya.
7. Catat kesalahan yang ditemukan dan cara memperbaikinya.

## Struktur Repository

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

## Keamanan dan Etika

- Jangan menyimpan password, token bot, atau API key langsung di source code.
- Gunakan environment variable dan file `.env` yang tidak di-commit.
- Jalankan proyek jaringan hanya pada aset milik sendiri atau yang telah memberikan izin.
- Gunakan proyek analisis log hanya pada data yang berhak kamu akses.
- Audit dan uji ulang sebelum menggunakan proyek pembelajaran di lingkungan production.

## Kontribusi

Issue dan pull request dipersilakan. Pastikan perubahan tetap mudah dipelajari, tidak menyertakan data sensitif, menjelaskan dependensi baru, dan telah diuji.

## Author

Dibuat dan dikelola oleh **Muhamad Dzarel Alghifari**.

- GitHub: [@DzarelDeveloper](https://github.com/DzarelDeveloper)
- Website: [dzarel.com](https://dzarel.com)

## Lisensi

Tersedia di bawah [MIT License](./LICENSE).

---

<div align="center">

**Belajar konsisten. Bangun sesuatu. Tingkatkan satu proyek setiap hari.**

</div>
