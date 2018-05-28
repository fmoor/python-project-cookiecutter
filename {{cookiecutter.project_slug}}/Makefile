.PHONY: help clean clean-pyc lint

help:
	@echo "clean - remove artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check for potential errors and poor style"
	@echo "test - runs the tests"
	@echo "quality - lint & test"

clean: clean-pyc

clean-pyc:
	find . -type f -name "*.py[co]" -delete
	find . -type f -name '*~' -delete
	find . -type d -name "__pycache__" -delete

lint:
	flake8 --config=flake8.ini
	mypy {{ cookiecutter.project_slug }} tests

test: clean
	pytest tests/

quality: lint test
