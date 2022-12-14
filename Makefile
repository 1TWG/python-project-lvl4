install:
	poetry install

make-requirements:
	poetry export -f requirements.txt --output requirements.txt

migrate:
	poetry run python manage.py migrate

setup:
	cp -n .env.example .env || true
	make install
	make migrate

start:
	poetry run python manage.py runserver

check:
	poetry check

lint:
	poetry run flake8 task_manager

test:
	poetry run python manage.py test

test-coverage:
	poetry run coverage run manage.py test python_django_blog
	poetry run coverage html
	poetry run coverage report

deploy:
	git push heroku main

locate:
	poetry run django-admin makemessages -l ru

compile:
	poetry run django-admin compilemessages

shell:
	poetry run python manage.py shell
