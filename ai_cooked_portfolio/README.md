# Kankunala Yamini - Portfolio (Python, Django, REST API, MySQL)

## Run locally
```
python -m venv venv
venv\Scripts\activate          # Windows  (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_projects
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000

- Admin (add/edit projects, read messages): /admin/
- Resume download (Django view): /resume/
- REST API: /api/profile/  /api/projects/  /api/contact/ (POST)

## Use MySQL
Set these environment variables before `migrate`:
`MYSQL_NAME, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT`
If MYSQL_NAME is not set, SQLite is used.
(Uses PyMySQL, so no extra C libraries are needed.)

## Deploy on Vercel
1. Create a hosted MySQL database (TiDB Cloud / Aiven). Save its CA certificate as `ca.pem` in the project root if SSL is required.
2. From your computer, set MYSQL_NAME, MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT and run:
   `python manage.py migrate`, `python manage.py seed_projects`, `python manage.py createsuperuser`
3. Push the project to GitHub.
4. In Vercel: Add New > Project > import the repo. Add environment variables:
   SECRET_KEY (long random string), DEBUG=0, and the five MYSQL_* variables. Deploy.
5. Add your own domain later via ALLOWED_HOSTS and CSRF_TRUSTED_ORIGINS (comma separated, CSRF needs https://).
