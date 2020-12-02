venv:
	poetry install

test: venv
	poetry run pytest

code-quality: venv
	poetry run pre-commit run --all-files
