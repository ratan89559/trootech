### Create virtual environment

```
$ python3 -m venv venv
```

### Activate virtual environment

```
$ source venv/bin/activate
```

### Install Requirements
```
Unzip the trootech.zip file
$ cd trootech
$ pip install -r requirements.txt

```

### Migration command Already completed (Optional)

```
$ python manage.py makemigrations
$ python manage.py migrate
```

### Run Django API server

```
$  python manage.py runserver
```

### Open in Browser

```
http://127.0.0.1:8000/swagger
http://127.0.0.1:8000/redoc
```
### Open Admin panel

```
http://127.0.0.1:8000/admin
username:admin
password:admin
```