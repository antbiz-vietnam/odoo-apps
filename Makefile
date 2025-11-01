# USE THIS ON LINUX OR MACOS, IF USING ON WINDOWS PLEASE USE WSL
include .env
.PHONY: docker

init:
	exec ./scripts/clone_from_odoo.sh

setup_dev:
	# prepare python3.11 before run this
	cd odoo && \
	python3.11 -m venv ./.venv && \
	./.venv/bin/activate && \ 
	pip install -r requirements.txt


DATE := $(shell date '+%Y%m%d%H%M%S')
docker_build:
	docker build --platform ${PLATFORM} -t odoo:latest -t odoo:$(DATE) -f ./docker/odoo.Dockerfile .

build:
	docker build --platform ${PLATFORM} -t odoo:latest -t odoo:$(DATE) -t odoo:$(GIT_HASH) -f ./docker/odoo.Dockerfile .

active_virtualenv:
	@echo "Please run this command to activate virtualenv"
	@echo ". ./odoo/.venv/bin/activate"

add_addons:
	# usage: make add_addons name=<module_name>
	./.venv/bin/python ./odoo/odoo-bin scaffold $(name) ./addons

start_local: docker_build
	docker compose -f ./docker/dockercompose.yaml up web db -d

update_submodule_all:
	# usage: make add_addons name=<module_name>
	make update_submodule name=helpdesk

update_submodule:
	git submodule update ./addons/$(name)

generate_pipeline:
	./.github/workflows/scripts/generate_deploy.sh

RELEASE_DATE := $(shell date '+%Y%m%d')
release:
	# usage: make release client=<client_name>
	echo "Releasing for client: $(client) on date: $(RELEASE_DATE)"
	git pull && git checkout origin/main && git tag releases/$(client)/$(RELEASE_DATE) && git push --tags