<<<<<<< HEAD
## Tujuan Sistem

Web digunakan sebagai **Project Roadmap Management System** untuk memonitor implementasi project dari fase preparation sampai final implementation.

Fitur utama:

* Menentukan Schedule Start & Finish
* Mengisi Actual Start & Finish
* Update Status (Scheduled, On Progress, Completed)
* Progress Tracking otomatis
* Komentar antar user
* Gantt Chart interaktif
* Drag & Drop Timeline
* CRUD Phase dan Task
* Audit History
* Multi User

---

# Flowchart Bisnis

```text
┌─────────────────┐
│     LOGIN       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Select Project  │
└────────┬────────┘
         │
         ▼
┌────────────────────────┐
│ Load Roadmap Project   │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ View All Phase         │
│ Preparation            │
│ Setup                  │
│ Integration            │
│ Training               │
│ Go Live                │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ Select Task            │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ Update Actual Date     │
│ Start / End            │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ Update Status          │
│ Scheduled              │
│ On Progress            │
│ Completed              │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ Add Comment            │
│ Discussion             │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ Auto Recalculate       │
│ Progress               │
│ Delay                  │
│ Variance               │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ Refresh Gantt Chart    │
└────────┬───────────────┘
         │
         ▼
┌────────────────────────┐
│ Save PostgreSQL        │
└────────────────────────┘
=======
# Enterprise Roadmap Pro | Fortunasuite Malioboro

Aplikasi manajemen roadmap proyek berbasis web interaktif dengan Gantt Chart, visualisasi periodik, dan pengelolaan tugas (Phases & Tasks) secara dinamis. Proyek ini dibangun dengan backend **FastAPI** dan frontend **Vue.js 3** + **Tailwind CSS**.

---

## 🚀 Fitur Utama

1. **Gantt Chart Interaktif & Responsif**:
   - Visualisasi jadwal rencana (*Planned*) dan realisasi (*Actual*) tugas secara berdampingan.
   - Fitur drag-and-drop dan resize bar untuk mengubah tanggal langsung dari grafik.
   - Pembedaan warna otomatis pada hari Sabtu dan Minggu (Merah & Magenta) serta penanda Hari Libur Nasional Indonesia.

2. **Roadmap Tools Manager (Terpusat)**:
   - Panel kontrol khusus yang diakses via tombol **Tools** di pojok kanan bawah.
   - **Kelompok / Phase**: Tambah, ubah nama, dan hapus phase secara langsung.
   - **Tugas / Sub-names**: Tambah tugas baru, hubungkan sebagai sub-task dari tugas induk, ubah nama, atau hapus tugas/subtask.

3. **Manajer Sub-task & Komentar**:
   - Fitur pengelolaan sub-task rinci dan komentar/remarks kolaboratif per departemen langsung pada remarks tugas.
   - Kolom progres tugas yang terhitung dinamis dari sub-task aktif.

4. **Sistem TDD (Test-Driven Development)**:
   - Pengujian terotomatisasi di sisi backend menggunakan `pytest` untuk menjamin stabilitas fungsionalitas CRUD.

---

## 🛠️ Persyaratan Sistem

- Python 3.10+
- Pip (Python Package Installer)
- Git (untuk kontrol repositori)

---

## 📦 Cara Instalasi

1. Clone repositori ke komputer lokal Anda:
   ```bash
   git clone https://github.com/Aldi451/RoadmapV2.git
   cd RoadmapV2
   ```

2. Instal dependensi yang diperlukan:
   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic pytest httpx
   ```

---

## ⚙️ Menjalankan Aplikasi

Anda dapat menggunakan script `.bat` yang telah disediakan untuk mempermudah operasional sehari-hari:

### 1. Menjalankan Server Lokal
Cukup klik ganda (double-click) berkas:
- **`run_server.bat`**
*Script ini akan otomatis mengaktifkan server FastAPI lokal pada `http://127.0.0.1:8000/` dan langsung membuka browser Anda.*

### 2. Mengunggah Perubahan ke GitHub
Untuk melakukan commit dan push secara cepat ke repositori GitHub:
- **`git_upload.bat`**
*Masukkan pesan commit Anda saat diminta, dan script akan melakukan git add, commit, dan push secara otomatis.*

### 3. Sinkronisasi & Pemulihan (Restore)
Untuk mengambil update terbaru dari GitHub atau memulihkan file lokal Anda jika terjadi error:
- **`git_restore.bat`**
  - **Opsi 1 (Update):** Melakukan `git pull` tanpa menghapus file lokal Anda.
  - **Opsi 2 (Restore):** Melakukan hard reset untuk mengembalikan seluruh codebase persis seperti di GitHub (menghapus perubahan lokal Anda).

---

## 🧪 Pengujian (TDD)

Backend dilengkapi dengan unit-test terintegrasi untuk memvalidasi endpoint API. Untuk menjalankan pengujian, jalankan perintah berikut di direktori root:
```bash
pytest
>>>>>>> 4744698 (perbaikan ke 2)
```

---

<<<<<<< HEAD
# Struktur Roadmap

```text
Project
│
├── Phase 1 Preparation
│     ├── Task 1
│     ├── Task 2
│     └── Task 3
│
├── Phase 2 Setup
│     ├── Task 1
│     ├── Task 2
│
├── Phase 3 Integration
│
├── Phase 4 Training
│
└── Phase 5 Go Live
```

---

# Flow Gantt Chart

```text
Scheduled Start
Scheduled End
        │
        ▼
Create Planned Bar
        │
        ▼
Actual Start
Actual End
        │
        ▼
Create Actual Bar
        │
        ▼
Compare Duration
        │
 ┌──────┴───────┐
 │              │
 ▼              ▼
On Time      Delayed
 │              │
 ▼              ▼
Green        Red
```

---

# Tampilan Tools

Di pojok kanan atas:

```text
[ + Add Phase ]
[ + Add Task ]
[ Edit ]
[ Delete ]
[ Import Excel ]
[ Export Excel ]
[ Export PDF ]
```

---

# Flow CRUD Phase

```text
Add Phase
    │
    ▼
Input Name
    │
    ▼
Save Database
    │
    ▼
Refresh Grid
```

---

# Flow CRUD Task

```text
Add Task
      │
      ▼
Select Phase
      │
      ▼
Input Task Name
      │
      ▼
Input Scheduled Date
      │
      ▼
Save
      │
      ▼
Generate Gantt Bar
```

---

# Flow Komentar

```text
User A
│
├─ "Training sudah selesai"
│
▼
Database
│
▼
Realtime Update
│
├─ User B melihat
├─ User C melihat
└─ User D membalas
```

Contoh:

```text
Task :
2.2 API Setup

Comments:

[Aldi]
API sudah aktif

[Fikri]
Sudah dicoba QA?

[Aldi]
Sudah berhasil
```

---

# Flow Drag Gantt

Yang menarik dari sistem ini:

### Cara 1

User ubah tanggal dari grid

```text
Actual Start
Actual End

▼

Gantt otomatis berubah
```

---

### Cara 2

User drag gantt

```text
Drag Bar →
```

Maka:

```text
Actual Start
Actual End

otomatis update
```

Jadi sinkron 2 arah.

```text
Grid ←→ Gantt Chart
```

---

# Hak Akses

## Admin

* Create Project
* Create Phase
* Create Task
* Delete Task
* Manage User

## Project Manager

* Edit Schedule
* Monitoring
* Comment

## Implementator

* Input Actual Date
* Update Status
* Comment

## Viewer

* Read Only
* Comment

---

# Database PostgreSQL

## projects

```sql
CREATE TABLE projects(
    id SERIAL PRIMARY KEY,
    project_name VARCHAR(255),
    customer_name VARCHAR(255),
    created_at TIMESTAMP
);
```

---

## phases

```sql
CREATE TABLE phases(
    id SERIAL PRIMARY KEY,
    project_id INT,
    phase_name VARCHAR(255),
    sort_order INT
);
```

---

## tasks

```sql
CREATE TABLE tasks(
    id SERIAL PRIMARY KEY,
    phase_id INT,
    task_name VARCHAR(255),

    scheduled_start DATE,
    scheduled_end DATE,

    actual_start DATE,
    actual_end DATE,

    status VARCHAR(50),

    progress INT
);
```

---

## comments

```sql
CREATE TABLE comments(
    id SERIAL PRIMARY KEY,
    task_id INT,
    user_id INT,
    comment TEXT,
    created_at TIMESTAMP
);
```

---

## users

```sql
CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    fullname VARCHAR(255),
    email VARCHAR(255),
    role VARCHAR(50)
);
```

---

# Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5
* FullCalendar
* Frappe Gantt / DHTMLX Gantt

### Backend

* Python
* FastAPI

### Database

* PostgreSQL

### Realtime

* WebSocket

### Hosting

* Frontend : Vercel
* Backend : Railway / Render
* Database : PostgreSQL

---

# Arsitektur Sistem

```text
HTML/CSS/JS
      │
      ▼
 FastAPI Backend
      │
 ┌────┼────┐
 │         │
 ▼         ▼
PostgreSQL WebSocket
 │         │
 ▼         ▼
Data     Realtime
          Comment
          Status
          Progress
```

=======
## 🌐 Dokumentasi API Endpoints

| Method | Endpoint | Deskripsi |
| :--- | :--- | :--- |
| **GET** | `/api/roadmap` | Mengambil seluruh data roadmap (Phase, Task, Subtask). |
| **POST** | `/api/roadmap/update-task` | Memperbarui atribut tugas (tanggal, status, note, progres, nama, dll). |
| **POST** | `/api/roadmap/phase` | Menambahkan kelompok/phase baru. |
| **POST** | `/api/roadmap/phase/{code}` | Mengubah nama kelompok/phase yang ada. |
| **DELETE** | `/api/roadmap/phase/{code}` | Menghapus kelompok/phase beserta seluruh tugas di dalamnya. |
| **POST** | `/api/roadmap/task` | Menambahkan tugas atau subtask baru. |
| **DELETE** | `/api/roadmap/task/{code}` | Menghapus tugas berdasarkan kodenya. |
| **GET** | `/api/holidays` | Mengambil daftar hari libur nasional. |
>>>>>>> 4744698 (perbaikan ke 2)
