# Django reminder project

#### This project is for educational purposes only.

---

##### To start the project you have to follow these steps:

1. `cp envs/.env.dev.template .env` - create environment config file for development purposes. Change `dev` to `test` or `stage` if you needed

2. `cp docker_composes/docker-compose.dev.yml.template docker-compose.yml` - create docker-compose config file. Change `dev` to `test.stage` if needed

3. `docker-compose up` - start the project environment (you can always use `-f` key to load another docker-compose.yml file)

    3.1. `manage.py runserver` - to start development mode server on your local machine

4. Go to http://127.0.0.1:8000/api/docs/ to see API docs after project starts or go to http://127.0.0.1:8000/admin/ to see Django Admin panel. Admin credentials: 
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

- Improve coverage
- Add Python type checking support
- Add code documentation
- Localize project
