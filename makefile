VENV_NAME := .venv
PYTHON := $(VENV_NAME)/scripts/python
PIP := $(VENV_NAME)/scripts/pip

# The default target when you run 'make'
.DEFAULT_GOAL := help

.PHONY: help venv install run test lint clean

help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  make %-15s %s\n", $$1, $$2}'

venv: ## Create a virtual environment if not exist
	@test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	@echo "Virtual environment created at $(VENV_NAME)."

install: venv ## Install project production and development dependencies
	$(PIP) install --upgrade pip
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi
	@if [ -f pyproject.toml ]; then $(PIP) install -e .; fi

run: venv 
	$(PYTHON) source\nsis_py\app.py

test: venv ## Run unit tests
	$(PYTHON) -m pytest

lint: venv ## Check code quality using ruff, flake8, or black
	$(PYTHON) -m ruff check .

clean: cleanup
	rm -rf .pytest_cache .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.py[co]" -exec rm -f {} +
	@echo "Cleanup complete."