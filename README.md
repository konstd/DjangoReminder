# Django reminder project

#### This project is for educational purposes only.

---

##### To start the project you have to follow these steps:

1. `cp .env.dev.template .env` - create environment config file for development purposes. Change `dev` to `test` or `stage` if you needed

2. `cp docker-compose.dev.yml.template docker-compose.yml` - create docker-compose config file. Change `dev` to `test.stage` if needed

3. `docker-compose up` - start the project environment

4. Go to http://127.0.0.1:8000/api/docs/ to see API docs after project starts or go to http://127.0.0.1:8000/admin/ to see Django Admin panel. Admin credentials: 
```
username: admin
email: admin@example.com
password: 1234567Q
```

If initial Admin user was not added add it by yourself:
```bash
cd service/
./manage.py shell
> from django.contrib.auth.models import User
> User.objects.create_superuser('admin', 'admin@example.com', '1234567Q')
```

### Development

If you want to continue development you need to install some pre-commit hooks:

```pre-commit install```

To check all files added to stage:

```pre-commit run --all-files```

### TODO:

- Improve UT coverage
- Change DB from PostgreSQL to MySQL
- Add Python type checking support
- Add code documentation
- Localize project
