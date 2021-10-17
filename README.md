# Supermarket

## Setup

Download: `git clone https://github.com/kuronosu/supermarket.git`

Move to the project folder: `cd supermarket`

Create virtual environment: `python -m venv venv`

Actiave virtual environment:
- Windows: `.\venv\Scripts\activate`
- Linux: `./venv/bin/activate`

Install dependencies: `pip install -r .\requirements.txt`

Create environment variable SECRET_KEY:

- Windows: `$env:SECRET_KEY="your-secret-key"`
- Linux: `export SECRET_KEY="your-secret-key"`

Run migrations: `python manage.py migrate`

Create superuser: `python manage.py createsuperuser`

Start server: `python manage.py runserver`

Note:

In each new terminal you must create the environment variable, you can do that and start the server with a single command

- Windows:  `$env:SECRET_KEY="your-secret-key" & python.exe manage.py runserver`
- Linux:  `SECRET_KEY="your-secret-key"; python.exe manage.py runserver`
