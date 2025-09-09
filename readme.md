# DriveSurat

Aplikasi Arsip Surat Digital

## Tujuan
DriveSurat adalah aplikasi web untuk mengelola arsip surat masuk/keluar secara digital, memudahkan pencarian, pengelompokan, dan pengunggahan surat berbasis PDF.

Aplikasi ini dibuat untuk memenuhi kebutuhan Ujian LSP Polinema

## Fitur
- Manajemen surat: upload, edit, hapus, lihat detail
- Kategori surat dinamis: tambah/edit/hapus kategori
- Pencarian surat berdasarkan judul
- Preview PDF langsung di browser
- Notifikasi sukses/gagal dengan toast
- File PDF tersimpan di folder media
- Otomatis load data contoh (fixture) saat build Docker
- Dukungan PostgreSQL (tidak menggunakan SQLite)

## Cara Menjalankan

### 1. Persiapan
- Pastikan Docker dan docker-compose terinstall
- Salin `.env.example` menjadi `.env` dan sesuaikan jika perlu

### 2. Build & Jalankan
```bash
docker compose up -d --build
```
Aplikasi akan otomatis migrate dan load data contoh jika database kosong.

### 3. Akses Web
Buka browser ke:
```
http://localhost:8000/
```

### 4. Manajemen Data
- Upload surat: menu "Arsip Surat >> Unggah"
- Tambah kategori: menu "Kategori Surat"
- File PDF tersimpan di folder `media/`


### 5. Screenshot

#### Halaman Tentang
![About Page](screnshoot/aboutpage.png)

#### Daftar Arsip Surat
![Arsip Surat](screnshoot/arsip_surat.png)

#### Edit Kategori Surat
![Edit Kategori](screnshoot/edit_kategori.png)

#### Edit Surat
![Edit Surat](screnshoot/editsurat.png)

#### Konfirmasi Hapus Surat
![Hapus Surat](screnshoot/hapus_surat.png)

#### Lihat Kategori
![Lihat Kategori](screnshoot/lihatkategori.png)

#### Lihat Surat
![Lihat Surat](screnshoot/lihatsurat.png)
![Lihat Surat 2](screnshoot/lihatsurat2.png)

#### Fitur Pencarian
![Search Bar](screnshoot/seachbar.png)

#### Tambah Kategori
![Tambah Kategori](screnshoot/tambahkategori.png)

#### Unduh Surat
![Unduh Surat](screnshoot/unduhsurat.png)

#### Unggah Surat
![Unggah Surat](screnshoot/unggah_surat.png)
![Unggah Surat Berhasil](screnshoot/unggah_surat.png_berhasil.png)
