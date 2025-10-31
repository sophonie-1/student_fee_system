# Student Fee Management System


A web-based application for managing student fees at Uganda Christian University, built as a full practical project using Django and Python. It supports student registration, fee structure setup, payment recording, balance computation, and summary reporting. Administrators can track payments efficiently and view total income/outstanding balances per program or campus.

This implementation uses Django's ORM for data persistence (SQLite by default), Class-Based Views (CBVs) for clean code, and Bootstrap for a responsive UI. All core features are implemented, plus bonuses like user authentication, search/filtering, and CSV export.

# Features

# Core Functionality
Student Management:
  - Add new students (student_id, name, program, campus, year_of_study).
  - View all registered students with balances and status.
  - Edit or delete student records (deletes cascade to payments).
Fee Structure Management:
  - Define fee structures per program/year (e.g., {"program": "BSc Computer Science", "year": 1, "total_fee": 2000000}).
  - Update fee amounts.
  - Display all fee structures.
Payment Recording:
  - Record payments (auto-generates payment_id like P001, includes student_id, amount, date).
  - Validates total payments do not exceed required fee (user-friendly error message on overpayment).
Balance Computation:
  - Per student: Total paid, balance = total_fee - total_paid.
  - Status: "Cleared" if balance=0, "Not Cleared" otherwise; "Fee Not Defined" if no matching fee.
# Summary Reporting
  - Per Student: Name, Program, Campus, Total Fee, Paid, Balance, Status.
  - Per Program: Total expected income, collected, outstanding balance.
  - Overall Summary: Total collected across all programs.

# Bonus Features
- Search and Filtering**: Search students by name, program, or campus.
- User Authentication**: Admin login required (uses Django's built-in auth; superuser via `createsuperuser`).
- Export Reports: CSV export of per-student report (downloadable from reports page).
- Error Handling : Input validation, overpayment prevention with contextual messages.
- Code Quality: Modular CBVs, readable templates, comments in models/views.

# Tech Stack
- Backend: Django 4.2+ (Python 3.8+), SQLite (default DB).
- Frontend: HTML templates with Bootstrap 5 for styling and responsive design.
- Other: Django forms for validation, CSV export via Python's `csv` module.

# Installation & Setup

1. # Prerequisites:
   - Python 3.8+.
   - Git (to clone repo).

2. # Clone the Repository:
   ```
   git clone https://github.com/sophonie-1/student_fee_system.git
   cd student_fee_system
   ```

3. # Set Up Virtual Environment:
   ```
   python -m venv venv
   # Activate (Windows): 

   venv\Scripts\activate
   # Activate (Mac/Linux):
   source venv/bin/activate
   ```

4. # Install Dependencies**:
   ```
   pip install django
   ```
    # installing project requirement packages run 
   ```
   pip install -r requirements.txt
   ```

5. **Run Migrations**:
   ```
   python manage.py makemigrations management
   python manage.py migrate
   ```

6. **Create Superuser** (for admin login):
   ```
   python manage.py createsuperuser
   ```
   - Enter username, email, and password.

7. # Run the Development Server:
   ```
   python manage.py runserver
   ```
   - Visit `http://127.0.0.1:8000/login/` to log in.
   - Use `/admin/` for quick data entry/testing.

# Usage

1. Log In: Use your superuser credentials at `/login/`.
2. Navigation: Use the top navbar (Students, Fees, Payments, Reports dropdown).
   - Students: Add/view/edit/delete students. Search via the form at bottom.
   - Fees: Add/update fee structures (per program/year).
   - Payments: Record payments (select student, enter amount—validation prevents overpay).
   - Reports:
     - Per Student: Detailed table + CSV export button.
     - Per Program: Aggregated income/outstanding.
     - Overall: Total collected.
3. Example Workflow:
   - Add a fee structure (e.g., BSc Computer Science, Year 1: 2,000,000 UGX).
   - Add a student (e.g., ID: S001, Name: John Doe, Program: BSc Computer Science, Campus: Main, Year: 1).
   - Record payments (e.g., 1,000,000 → Balance: 1,000,000, Status: Not Cleared).
   - Full payment → Status: Cleared.
   - View reports for summaries.


author :Bukira sophonie
# you can use these crendentials for login

`` username : bukira ``
``password : 123 ``
