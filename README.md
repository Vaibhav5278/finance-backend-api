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

