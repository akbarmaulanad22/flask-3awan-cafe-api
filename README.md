# 3awan Cafe API — Flask + PostgreSQL (Railway)

Backend API untuk aplikasi 3awan Cafe.  
Menggunakan Flask, SQLAlchemy, dan PostgreSQL yang di-host di Railway.

---

## 🏁 Cara Memulai

### 1. Clone Repository
```bash
git clone https://github.com/akbarmaulanad22/flask-3awan-cafe-api.git

cd flask-3awan-cafe-api
```
### 2. Install Dependencies
``` bash
pip install -r requirements.txt
```

### 3. Konfigurasi Database di file config/database.py
Ubah Koneksi sesuai link PostgreSQL yang kamu buat di Railway.

### 4. Jalankan Server di Lokal
```bash
python app.py
```

Akses:
```bash
http://127.0.0.1:5000
```

🚀 Deploy ke Railway (Via GitHub)
Login ke Railway menggunakan akun GitHub

```bash
https://railway.app
```

Klik New Project

Pilih repo yang sudah di clone

Pilih Deploy from GitHub Repo
flask-3awan-cafe-api

Railway akan otomatis build & menjalankan API.

Setelah berhasil, Railway akan memberikan domain, misalnya:

```bash
https://3awan-cafe-api.up.railway.app
```
Gunakan domain ini di Flutter (menu_service.dart / order_service.dart).

## 📡 API Endpoints

### 🍽️ Menu
| Method | Endpoint        | Deskripsi         |
|-------|----------------|---------------------|
| GET   | `/menus`       | Ambil semua menu    |
| POST  | `/menus`       | Tambah menu baru    |
| PUT   | `/menus/<id>`  | Update menu         |
| DELETE| `/menus/<id>`  | Hapus menu          |

### 🛒 Orders
| Method | Endpoint         | Deskripsi            |
|--------|-----------------|-----------------------|
| GET    | `/orders`       | Ambil semua pesanan   |
| POST   | `/orders`       | Buat pesanan baru     |


📂 Struktur Folder
```css
flask-3awan-cafe-api/
│ app.py
│ requirements.txt
│
├── config/
│   └── database.py
├── models/
│   └── menu.py
│   └── order.py
├── controllers/
│   └── menu_controller.py
│   └── order_controller.py
└── routes/
    └── web.py
```