build:
	docker-compose build
run:
	docker-compose up -d
start:
	make build; make run; make upgrade
migrate:
	docker-compose exec backend flask db migrate -m "$(message)"
upgrade:
	docker-compose exec backend flask db upgrade
freeze:
	pip freeze > requirements.txt
logs:
	docker-compose logs
