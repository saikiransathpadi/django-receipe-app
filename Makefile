docker_up:
	docker-compose up

docker_down:
	docker-compose down

docker_build:
	docker-compose build

test:
	docker-compose run --rm app sh -c 'python manage.py wait_for_db && python manage.py test'

make_migrations:
	docker-compose run --rm app sh -c 'python manage.py makemigrations'

migrate:
	docker-compose run --rm app sh -c 'python manage.py wait_for_db && python manage.py migrate'

lint_check:
	docker-compose run --rm app sh -c 'flake8 .'

create_superuser:
	docker-compose run --rm app sh -c 'python manage.py createsuperuser'
