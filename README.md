# Tugas Besar IF2121 Logika Komputasional
> Sebuah compiler sederhana untuk bahasa pemrograman Python

## Daftar Isi
* [Informasi Umum](#informasi-umum)
* [Teknologi yang Dipakai](#teknologi-yang-dipakai)
* [Fitur](#fitur)
* [Setup](#setup)
* [Daftar File](#daftar-file)
* [Penggunaan](#penggunaan)
* [Status Proyek](#status-proyek)
* [Ruang Perbaikan](#ruang-perbaikan)
* [Apresiasi](#apresiasi)
* [Kontak](#kontak)

## Informasi Umum
Program ini dibuat untuk memenuhi tugas Mata Kuliah IF2124 Teori Bahasa Formal dan Otomata

*Program Studi Teknik Informatika* <br />
*Sekolah Teknik Elektro dan Informatika* <br />
*Institut Teknologi Bandung* <br />

*Semester I Tahun 2021/2022*

Secara umum kami membuat grammar dalam bentuk CFG yang selanjtunya diubah menjadi CNF dengan
menggunakan program kemudian mengubah kode Python yang akan dicek sintaksnya ke dalam token
lalu mencocokkan tokennya dengan grammar.

## Teknologi yang Dipakai
- Python - 3.9.0

## Fitur
Program ini memiliki beberapa fitur, yaitu:
- Dapat mengecek kesalahan sintaks pada kode Python
- Dapat menampilkan baris letak kesalahannya

## Setup
- Persyaratan dasar
    - Install [Python](https://www.python.org/downloads/)
    - Unduh repository ini dalam bentuk .zip
    - Ekstrak zip ke lokasi yang diinginkan
- Cara Eksekusi Program
    - Jalankan program dengan nama file main.py

## Daftar File
- `cfg.txt` -> berisi grammar CFG
- `cnf.txt` -> berisi production rules yang sudah diubah menjadi CNF dengan program
- `cfg_to_cnf.py` -> berisi fungsi-fungsi untuk mengubah CFG menjadi CNF
- `cyk.py` -> berisi fungsi-fungsi untuk melakukan algoritma CYK
- `main.py` -> program utama
- `tokenizer.py` -> berisi fungsi-fungsi untuk mengubah kode Python menjadi token
- semua file yang tidak disebutkan di atas artinya merupakan kode Python yang akan dicek sintaksnya.

## Penggunaan
1. Jalankan program main.py.
2. Masukkan nama file Python yang mau dicek sintaksnya.
3. Tunggu untuk beberapa waktu sampai muncul pesan.
4. Jika ingin mengubah grammar, dapat mengedit `cfg.txt`.
5. Jika file Python yang mau dicek belum ada, bisa membuat file baru pada direktori file yang sama dengan main.py.

## Status Proyek
_Proyek Selesai_

## Ruang Perbaikan
Terdapat hal-hal yang dapat dikembangkan dari proyek ini, diantaranya:
- Mempercepat efisiensi waktu dari algoritma
- Menambah fitur yang menunjukkan letak kesalahan per karakter
- Menambah warna pada pesan kesalahan

## Apresiasi
Kami sangat berterima kasih kepada
- Ibu Ayu Purwarianti, yang telah memberikan kami pengajaran mengenai Teori Bahasa Formal dan Otomata,
- Asisten,
- Mata kuliah lain yang memberikan tugas besar di saat yang bersamaan sehingga mewarnai masa-masa pengembangan program,
- Mata dan otak yang panas tiap saat,
- Mental yang hampir jatuh selama pengerjaan, dan
- Laptop yang menyala 24/7.

## Kontak
Dibuat oleh
- [@Fayza Nadia](https://github.com/fayzanadia) - 13520001
- [@Nadia Mareta Putri L.](https://github.com/KorbanFidas2A) - 13520007
- [@Muhammad Helmi Hibatullah](https://github.com/mhelmih) - 13520014
