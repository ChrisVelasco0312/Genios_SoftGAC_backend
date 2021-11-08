setup:
	pip install -r requirements.txt

server:
	cd SoftGAC && python manage.py runserver

migrations:
	cd SoftGAC && python manage.py makemigrations

migrate:
	cd SoftGAC && python manage.py migrate
