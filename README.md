

```markdown
# CodeAlpha_SimpleStore

![CodeAlpha Task 1](https://img.shields.io/badge/CodeAlpha-Task_1-blue.svg)

Task 1 - E-commerce store (name: simplestore) for @CodeAlpha.

## File/Folder Structure
```text
CodeAlpha_SimpleStore/
│
├── my_store/            # Django project configuration folder
│   ├── __init__.py      # Marks directory as a Python package
│   ├── asgi.py          # ASGI config for async web servers
│   ├── settings.py      # Main Django settings (installed apps, database config, etc.)
│   ├── urls.py          # Project-level URL declarations
│   └── wsgi.py          # WSGI config for deployment
│
├── shop/                # Main Django application folder handling store logic
│   ├── migrations/      # Database migrations for the shop app
│   ├── templates/       # HTML templates for the frontend
│   ├── __init__.py      # Marks directory as a Python package
│   ├── admin.py         # Django admin panel configuration
│   ├── apps.py          # App configuration
│   ├── models.py        # Database models (e.g., Products, Orders)
│   ├── tests.py         # Unit tests
│   └── views.py         # Views handling request logic and returning HTTP responses
│
├── .gitignore           # Specifies intentionally untracked files to ignore
├── manage.py            # Django command-line utility for administrative tasks
└── README.md            # Project documentation (this file)
```

## Technologies & Languages Used
* **Python**: Core backend programming language.
* **Django**: High-level Python web framework used to build the application.
* **HTML**: Used in Django templates for building the frontend pages.
* **SQLite**: Default relational database provided by Django.

## Features
* A simple e-commerce storefront allowing users to browse products.
* Built using the robust Django framework.

## How to Run It

### 1. Clone the repository
Open your terminal and run:
```bash
git clone https://github.com/healerfatim/CodeAlpha_SimpleStore.git
cd CodeAlpha_SimpleStore
```

### 2. Set up a Virtual Environment (Optional but recommended)
```bash
python -m venv venv
```
Activate the virtual environment:
* **Windows**: `venv\Scripts\activate`
* **macOS/Linux**: `source venv/bin/activate`

### 3. Install Requirements
Install Django:
```bash
pip install django
```

### 4. Apply Database Migrations
Initialize the SQLite database with the required schema:
```bash
python manage.py migrate
```

### 5. Create a Superuser (Admin Access)
To access the Django admin panel, you (or your teacher) will need to create a superuser account. 
Run the following command and follow the prompts to set a username, email, and password:
```bash
python manage.py createsuperuser
```

### 6. Run the Development Server
Start the local server:
```bash
python manage.py runserver
```
Once the server is running:
* **Main Site**: Navigate to `http://127.0.0.1:8000/`
* **Admin Panel**: Navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials you just created.
```
