#!/bin/bash

# sleep before indexing
sleep 12

if [ $DJANGO_DEBUG = "true" ]; then
    echo "[START] install dependencies"
    pip install -r requirements.txt
fi

echo "[START] apply migrations"
python manage.py migrate

if [ $PRERUN = "true" ]; then
    echo "[START] run preinit script"
    echo "exec(open('prerun.py').read())" | python manage.py shell
fi

if [ $PYTHON_DEBUG = "true" ]; then
    /usr/sbin/sshd -D
else
    if [ $DJANGO_RUN_TESTS = "true" ]; then
      python manage.py test
      coverage report -m --skip-covered
      coverage xml -i -o reports/coverage.xml
      sed -i 's_/app_src_g' /app/reports/coverage.xml
      chmod -R 777 reports/
    fi

    if [ $DJANGO_DEBUG = "true" ]; then
        echo "[START] launch sshd"
        /usr/sbin/sshd
        echo "[START] launch app in debug mode"
        python manage.py runserver 0.0.0.0:8000
    else
        echo "[START] collect static resources"
        python manage.py collectstatic --noinput --clear

        echo "[START] launch app in release mode"
        uwsgi --chdir=. \
          --module=core.wsgi:application \
          --env DJANGO_SETTINGS_MODULE=core.settings \
          --master \
          --http=0.0.0.0:8000 \
          --processes=5 \
          --uid=1000 --gid=2000 \
          --harakiri=20 \
          --max-requests=5000 \
          --vacuum
    fi
fi
