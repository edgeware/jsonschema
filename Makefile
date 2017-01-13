VIRTUALENV ?= env
TOXBIN ?= $(VIRTUALENV)/bin/tox

all: help

.PHONY: help
help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  test       run all unit tests"

test: $(VIRTUALENV)
	$(TOXBIN)

$(VIRTUALENV):
	virtualenv $@
	$@/bin/pip install tox
