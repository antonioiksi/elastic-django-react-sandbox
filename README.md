#This is a sandbox for Elasticksearch, Django, Postgres and Reactjs

```
requirements
+ python3.5

```

## STEP 1 create simple django project with postgres
let us create <mark>backend</mark> project

```commandline
django-admin startproject backend
```

then create database and user with  privileges, for this you can run script `scripts/create-db.sh`
or connect to database management system and do it like I did in Postgres
```commandline
psql
```
```postgresplsql
CREATE USER user171030 WITH PASSWORD 'user171030';
ALTER ROLE user171030 SET client_encoding TO 'utf8';
ALTER ROLE user171030 SET default_transaction_isolation TO 'read committed';
ALTER ROLE user171030 SET timezone TO 'UTC';
ALTER USER user171030 CREATEDB;


CREATE DATABASE user171030;
GRANT ALL PRIVILEGES ON DATABASE user171030 TO user171030;

```

and now write down connect to database in django app settings `backend/backend/settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'user171030',
        'USER': 'user171030',
        'PASSWORD': 'user171030',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```

```commandline
cd backend
python manage.py migrate
```
let's check our backend is working!!!
```commandline
python manage.py runserver
```

rememeber names of our packages in requirements.txt
```commandline
pip freeze > requirements.txt
```

## STEP 2 Setup JWT Auth for django project

```commandline
cd backend

pip install coreapi djangorestframework \
      djangorestframework-simplejwt
```

change  install apps in `settings.py`
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]

# Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}
```

now let us make some changes in `urls.py` (have a look in git repo)

Now start up server!
```commandline
./manage.py runserver
```


## 4 STEP create test rest api SECURE and INSECURE

```commandline
cd backend && ./manage.py startapp app_log
```

in file `app_log/models.py` create model

add app in backend/settings.py
```python
INSTALLED_APPS = [
    ...
    'app_log',
]
```
TODO add description


## 5 STEP Load data


./manage.py loaddata attributes.json 



## **Allow problem

`pip install django-cors-headers`

than add to settings.py

```python

INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    ...
] 
```

# FRONTEND

from the root of our project execute

```commandline
mkdir frontend && cd frontend
create-react-app .

```

```commandline
npm i --save bootstrap
npm i --save react-bootstrap

```
add routes
```commandline
npm i --save react-router-dom
```