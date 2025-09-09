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

#### Tampilan Upload Surat
![arsip_surat](<img width="1920" height="961" alt="image" src="https://github.com/user-attachments/assets/f80ee4bf-bf37-4c00-a6e0-394d84061452" />)

### Tampilan Saat Upload Surat diisi dan berhasil
![upload Surat berhasil](<img width="1920" height="585" alt="image" src="https://github.com/user-attachments/assets/074dd6fd-907a-454c-8e51-24c418cd36d3" />)

#### Tampilan Daftar Surat
![upload_surat](<img width="1920" height="970" alt="image" src="https://github.com/user-attachments/assets/32384eb3-ae13-4903-af41-134e9914b28f" />)

### Tampilan Saat delete Surat
![delete_surat](<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1145d812-2204-44c3-872f-de85b0caa89e" />)

### Tampilan Lihat Surat
![detail_surat]()

#### Tampilan Kategori Surat
![kategori_surat](<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/9c21992e-e3cb-4d16-b0b6-9602c6f95972" />)
![kategori_surat](<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/18f45d70-15bc-4162-863f-8cacd5756eba" />)

---
