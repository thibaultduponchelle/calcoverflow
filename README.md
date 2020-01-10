# Calcoverflow

A shitty questions/answers site.

## Setup (python3 + django latest)

```

# Setup python
apt-get install python3-venv
apt-get install python3-pip # Probably not needed because venv could probably do it for us (?)
apt-get install python3-pymysql
apt-get install python3-mysqldb

# Virtual env
python3 -m venv ~/DjangoLatest
source ~/DjangoLatest/bin/activate

# Requirements
pip install Django
pip install django_registraton
pip install pymysql
pip install markdown
pip install wheel
pip install mysqlclient

# Install DB 
sudo apt-get install default-libmysqlclient-dev libmysqlclient-dev libmysqlclient20 python-mysqldb
su 
mysql -u root -p
(Do not type anything)
ALTER USER 'tib'@'localhost' IDENTIFIED BY 'pass';
FLUSH PRIVILEGES;

# Start service
python manage.py migrate
python manage.py createsuperuser
python manage runserver
```

## Old Setup

### Optional

```bash
virtualenv ~/Django1.11.25
source ~/Django1.11.25/bin/activate
```

### Install Django and co

```bash
sudo apt-get install libssl-dev
pip install Django==1.11.25
pip install django-registration==2.4.1
pip install pymysql mysql-python
pip install markdown
# Ubuntu 18
sudo apt-get install default-libmysqlclient-dev libmysqlclient-dev libmysqlclient20 python-mysqldb mysql-client-core-5.7 mysql-server 
su 
mysql -u root
CREATE USER 'tib'@'localhost' IDENTIFIED BY 'pass';
OR eventually if user already exists :
ALTER USER 'tib'@'localhost' IDENTIFIED BY 'pass';
CREATE DATABASE calcoverflow;
GRANT ALL PRIVILEGES ON calcoverflow.* TO 'tib'@'localhost';
FLUSH PRIVILEGES;
```

### Run

```bash
python manage.py runserver
```
