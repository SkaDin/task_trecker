build_image:
	docker-compose up --env-file .env

check_lint:
	black .
	ruff check
	isort .
