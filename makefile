# Define variables to ensure consistency across tasks
VENV_NAME := .venv
PYTHON := $(VENV_NAME)/bin/python
PIP := $(VENV_NAME)/bin/pip

# The default target when you run just 'make'
.DEFAULT_GOAL := help

.PHONY: help venv install run test lint clean

help: ## Show this help message with descriptions
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  make %-15s %s\n", $$1, $$2}'

venv: ## Create a virtual environment if it does not exist
	@test -d $(VENV_NAME) || python3 -m venv $(VENV_NAME)
	@echo "Virtual environment created at $(VENV_NAME)."

install: venv ## Install project production and development dependencies
	$(PIP) install --upgrade pip
	@if [ -f requirements.txt ]; then $(PIP) install -r requirements.txt; fi
	@if [ -f pyproject.toml ]; then $(PIP) install -e .; fi

run: venv ## Run the main application script
	$(PYTHON) source\nsis_py\app.py

test: venv ## Run unit tests using pytest
	$(PYTHON) -m pytest

lint: venv ## Check code quality using ruff, flake8, or black
	$(PYTHON) -m ruff check .

clean: ## Remove temporary Python cache files and build artifacts
	rm -rf .pytest_cache .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.py[co]" -exec rm -f {} +
	@echo "Cleanup complete."