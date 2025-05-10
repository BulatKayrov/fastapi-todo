DIR ?= .
FILES := $(DIR)/views.py $(DIR)/service.py $(DIR)/repository.py $(DIR)/utils.py $(DIR)/schemas.py
m ?= "initial migration"
dir_name ?= alembic
r ?= 1

.PHONY: create_file
create_file:
	touch $(FILES)
	@echo "Files created: $(FILES)"


.PHONY: upgrade
upgrade:
	alembic revision --autogenerate -m "$(m)" && alembic upgrade head

.PHONY: alembic-init
alembic-init:
	alembic init -t async $(dir_name)

.PHONY: rollback
rollback:
	alembic downgrade -$(r)
