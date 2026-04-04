# finance-backend-api

# 💰 Finance Data Processing & Access Control Backend

> A robust backend system built with Django REST Framework to manage financial records with role-based access control and real-time analytics.

---

## 📌 Project Overview

This project implements a scalable backend for a finance dashboard system.  
It enables secure handling of financial transactions with role-based permissions and provides aggregated insights for decision-making.

---

## ✨ Key Features

### 🔐 Authentication & Authorization
- Custom User Model
- Role-Based Access Control (RBAC)
- Roles:
  - **Admin** → Full access (CRUD + user management)
  - **Analyst** → Read access + analytics
  - **Viewer** → Read-only access
- Session-based authentication

---

### 💵 Financial Records Management
- Full CRUD operations
- Structured financial data:
  - Amount
  - Type (Income / Expense)
  - Category
  - Date
  - Notes
- Data filtering and querying support

---

### 📊 Dashboard & Analytics
- Total Income Calculation
- Total Expense Calculation
- Net Balance Computation
- Aggregated financial insights via API

---

### 🔒 Access Control
- Endpoint-level permission enforcement
- Role-specific restrictions using custom permission classes

---

### ⚠️ Validation & Error Handling
- Input validation using serializers
- Meaningful API responses
- Proper HTTP status codes

---

## 🛠️ Tech Stack

| Layer        | Technology                  |
|-------------|---------------------------|
| Backend     | Django                    |
| API         | Django REST Framework     |
| Database    | SQLite                    |
| Language    | Python                    |

---

## Output:
<img width="1919" height="910" alt="Screenshot 2026-04-02 104225" src="https://github.com/user-attachments/assets/312b9c6a-6bba-442a-ad29-376c5f4ba4cc" />

<img width="1910" height="918" alt="Screenshot 2026-04-02 104154" src="https://github.com/user-attachments/assets/0e4a36a3-be26-4c8e-b376-8b60bf82ad19" />

<img width="1864" height="763" alt="Screenshot 2026-04-02 102650" src="https://github.com/user-attachments/assets/dc0e1054-431c-4f5c-8fb4-4d8d2d40ebfb" />



