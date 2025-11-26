PYTHON ?= python3
VENV ?= .venv
ACTIVATE = source $(VENV)/bin/activate

.PHONY: venv install lint format test check clean

venv:
	$(PYTHON) -m venv $(VENV)
	$(ACTIVATE) && pip install --upgrade pip

install: venv
	$(ACTIVATE) && pip install -r requirements.txt

lint:
	$(ACTIVATE) && ruff check src tests

format:
	$(ACTIVATE) && ruff format src tests

test:
	$(ACTIVATE) && pytest

check: lint test

clean:
	rm -rf $(VENV) .pytest_cache .ruff_cache
