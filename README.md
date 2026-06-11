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
```

---

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

