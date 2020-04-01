# Django reminder project

#### This project is for educational purposes only.

Django reminder service includes such API functionality as:
- user registration
- user authentication
- user profile
- user can create, update and delete reminders
- async celery task will send notification to user when time will come over email
- user can attach another users to reminder
- user can watch his reminders where he is the author and also where he participates
- user can mark reminder as completed
- Reminder contain these fields: title, body, location, participants, creation date, target date

Main technical stack:
- Python 3.8, Django 3, DRF, Django Signals
- PostgreSQL 11
- Docker
- Celery

---

##### To start the project you have to follow these steps:

1. `docker-compose up -f docker-compose-dev.yml` - start the dev project environment

    1.1. Install `virtualenv` for development environment and activate it

    1.2. Use `manage.py runserver` - to start development mode server on your local machine

2. `docker-compose up -f docker-compose-stage.yml` - start stage project environment with internal docker server (django tests + coverage)

3. Go to http://127.0.0.1:8000/api/docs/ to see API docs after project starts or go to http://127.0.0.1:8000/admin/ to see Django Admin panel. Admin credentials: 
```
username: admin
email: admin@example.com
password: 1234567Q
```

If initial Admin user was not added add it by yourself:
```bash
cd service/
./manage.py createsuperuser
```

### Development

If you want to continue development you need to install some pre-commit hooks:

```pre-commit install```

To check all files added to stage:

```pre-commit run --all-files```

### TODO:

- Celery worker is not working as expected in dev mode for now. Need to fix it
- Improve coverage
- Add Python type checking support
- Add code documentation
- Localize project
