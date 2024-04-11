.PHONY: install
install:
	poetry install

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall
	poetry run pre-commit install

.PHONY: lint
lint:
	poetry run pre-commit run --all-files

.PHONY: test
test:
	poetry run pytest -r -va -b render core

.PHONY: migrations
migrations:
	poetry run python -m msd.manage makemigrations

.PHONY: migrate
migrate:
	poetry run python -m msd.manage migrate

.PHONY: run-server
run-server:
	poetry run python -m msd.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m msd.manage createsuperuser

.PHONY: up-dependencies-only
up-dependencies-only:
	if not exist .env (type nul > .env)
	docker-compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: update
update: install migrations migrate install-pre-commit ;
