.PHONY: help clean clean-pyc lint

help:
	@echo "clean - remove Python file artifacts"
	@echo "flake8 - check for potential errors and poor style"
	@echo "mypy - check for potential type errors"
	@echo "lint - flake8 & mypy"
	@echo "test - runs the tests"
	@echo "coverage - check for untested code"
	@echo "quality - lint, test & coverage"

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type f -name '*~' -delete
	find . -type d -name "__pycache__" -delete

flake8:
	flake8

mypy:
	mypy {{ cookiecutter.project_slug }} tests

lint: flake8 mypy

test: clean
	pytest -vv tests/

coverage: clean
	pytest tests/ \
	  --cov={{ cookiecutter.project_slug }}/ \
	  --cov-report term-missing:skip-covered

quality: lint clean
	pytest tests/ \
	  -vv \
	  --cov={{ cookiecutter.project_slug }}/ \
	  --cov-report=term-missing:skip-covered
