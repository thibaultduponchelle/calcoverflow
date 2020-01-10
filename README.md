# Calcoverflow

## Setup

### Optional

```bash
virtualenv ~/Django1.11.25
source ~/Django1.11.25/bin/activate
```

### Install Django and co

```bash
pip install Django==1.11.25
pip install django-registration
pip install pymysql
# Ubuntu 18
sudo apt-get install default-libmysqlclient-dev libmysqlclient-dev libmysqlclient20 python-mysqldb mysql-client-core-5.7 mysql-server 
su 
mysql -u root
(Do not type anything)
ALTER USER 'tib'@'localhost' IDENTIFIED BY 'pass';
FLUSH PRIVILEGES;
pip install markdown
```

### Run

```bash
python manage.py runserver
```
