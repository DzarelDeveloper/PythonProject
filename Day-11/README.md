# Day 11 — Multi-Function Timer

**Level:** Menengah  
**Fokus:** state aplikasi, waktu, callback

## Tujuan Belajar

Menggabungkan stopwatch, countdown, atau alarm. Setelah menyelesaikan hari ini, kamu diharapkan mampu menjelaskan alur program, menjalankannya sendiri, dan memodifikasi setidaknya satu fiturnya.

## Konsep yang Dipelajari

- state aplikasi
- waktu
- callback
- Memecah masalah menjadi input, proses, dan output
- Membaca pesan error serta melakukan debugging dasar

## Persiapan

**Kebutuhan:** Tidak ada; Tkinter biasanya sudah tersedia

Gunakan virtual environment agar dependensi proyek tidak bercampur dengan instalasi Python sistem.

```bash
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Jika `main.py` mengimpor library yang belum tersedia, instal package yang disebutkan pada bagian kebutuhan.

## Menjalankan Proyek

Dari root repository:

```bash
cd Day-11
python main.py
```

## Alur Program

1. Program memuat module dan menyiapkan data atau antarmuka yang diperlukan.
2. Input diterima dari pengguna, file, perangkat, atau layanan eksternal sesuai fungsi proyek.
3. Fungsi utama memvalidasi dan memproses input.
4. Hasil ditampilkan melalui terminal, GUI, file, atau respons HTTP.
5. Error harus ditangani dengan pesan yang membantu pengguna memperbaiki input atau konfigurasi.

Buka `main.py`, temukan titik awal program, lalu ikuti pemanggilan fungsi secara berurutan. Perhatikan variabel yang menyimpan state serta bagian yang berinteraksi dengan sistem di luar program.

## Eksperimen Hari Ini

- Jalankan versi asli dan catat hasilnya.
- Ubah satu teks, nilai awal, atau konfigurasi kecil.
- Berikan satu input valid dan satu input tidak valid.
- Tambahkan satu `print()` sementara untuk melihat aliran data.
- Kembalikan kode setelah selesai melakukan debugging.

## Tantangan

Tambahkan notifikasi suara dan preset timer.

## Checklist

- [ ] Program dapat dijalankan
- [ ] Saya memahami input, proses, dan output
- [ ] Saya dapat menjelaskan fungsi utama
- [ ] Saya menguji kondisi input yang salah
- [ ] Saya menyelesaikan minimal satu modifikasi
- [ ] Tidak ada credential atau data sensitif di dalam kode

## Catatan

Proyek ini ditujukan untuk pembelajaran. Tinjau validasi, keamanan, error handling, dan pengujian sebelum menggunakannya untuk kebutuhan nyata.
