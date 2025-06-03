# TheFinanceApp
Fully Feature Set Finance Platform for projecting cashflows budgets and other things for your personal networth.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Apply migrations:
   ```bash
   cd finance_project
   python manage.py migrate
   ```

3. Run development server:
   ```bash
   python manage.py runserver
   ```

The finance app exposes simple CRUD screens at `/income/`, `/expense/`, `/asset/`, and `/liability/`.
