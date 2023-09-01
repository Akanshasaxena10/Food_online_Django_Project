dev-start:##to run
	python manage.py runserver --settings=config.settings.dev
dev-install:
	pip install -r requirements/dev.txt
dev-makemigrations:##To create
	python manage.py makemigrations --settings=config.settings.dev
dev-migrate:##To establish
	python manage.py migrate --settings=config.settings.dev
dev-showmigrations:
	python manage.py showmigrations --settings=config.settings.dev