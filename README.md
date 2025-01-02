### Step 1: Set Up the Virtual Environment

1. Clone the repository.  
2. Use `pipenv` to manage a virtual environment for the Django app.  
   - Install `pipenv` globally (if not already installed): `brew install pipenv`  
3. Configure `pipenv` to use a directory you have access to (helpful for company laptops):  
   - Open the shell configuration file: `nano ~/.zshrc`  
   - Add the configuration line at the bottom: `export PIPENV_VENV_IN_PROJECT=true`  
   - Reload the shell configuration: `source ~/.zshrc`  
4. Activate the virtual environment and create a `.venv` folder in the project directory: `pipenv shell`  

### Step 2: Install Django

1. Install Django using `pipenv`: `pipenv install Django`  
2. Verify the installation: Run `django-admin` in the terminal to confirm it is available.  
3. Start the development server: `python3 manage.py runserver`  
4. Apply database migrations: `python3 manage.py migrate`  

---

### Step 3: Set Up PostgreSQL and psycopg2

#### A. PostgreSQL Installation (Outside the Virtual Environment)  

1. Install PostgreSQL: `brew install postgresql`  
2. Ensure PostgreSQL is running globally: `brew services start postgresql`  

#### Optional: Test PostgreSQL Setup  

1. Access the PostgreSQL CLI: `psql postgres`  
2. Create a database: `CREATE DATABASE mydatabase;`  
3. Create a user with a password: `CREATE USER myuser WITH PASSWORD 'mypassword';`  
4. Grant privileges to the user: `GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;`  
5. Exit the PostgreSQL CLI: `\q`  

#### B. Back to the App  

1. Restart the `pipenv` shell: `pipenv shell`  
2. Install `psycopg2-binary`: `pipenv install psycopg2-binary`  
3. Create the database for your app: `createdb cocktails`  
4. Apply migrations:  
   - Create migrations: `python manage.py makemigrations`  
   - Apply migrations: `python manage.py migrate`  
5. Start the development server: `python manage.py runserver`  

---

### Step 4: Test Database Connection

1. Open a new terminal in the same environment.  
2. Ensure the database connection works: `python manage.py dbshell`  

---

### Note: `dbshell` vs. `shell`

- Use `dbshell` to work directly with raw SQL on the database.  
- Use `shell` to interact with your Django project in Python, leveraging its ORM and settings.