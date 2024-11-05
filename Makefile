DC = docker compose
LOGS = docker logs

APP_DEV = docker_compose/app.dev.yaml
STORAGES = docker_compose/storages.yaml
MIGRATE = docker_compose/migrate.yaml
ENV_FILE = --env-file .env

.PHONY: app-dev
app-dev:
	${DC} -p fastapi-user -f ${APP_DEV} ${ENV_FILE} up --build -d

.PHONY: storages
storages:
	${DC} -p fastapi-user -f ${STORAGES} ${ENV_FILE} up -d --build

.PHONY: storages-down
storages-down:
	${DC} -p fastapi-user -f ${STORAGES} ${ENV_FILE} down

.PHONY: down-dev
down-dev:
	${DC} -p fastapi-user -f ${APP_DEV} ${ENV_FILE} down

.PHONY: down
down:
	${DC} -p fastapi-user -f ${APP_DEV} -f ${STORAGES} ${ENV_FILE} down

.PHONY: migrate
migrate:
	${DC} -p fastapi-user -f ${MIGRATE} ${ENV_FILE} up --build
	${DC} -p fastapi-user -f ${MIGRATE} ${ENV_FILE} down

.PHONY: test
test:
	${DC} -p fastapi-user -f ${APP_DEV} ${ENV_FILE} exec main-app pytest -v
