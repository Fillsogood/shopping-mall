@echo off

poetry run black .
poetry run isort .
poetry run mypy .
@REM poetry run mypy --explicit-package-bases apps/
@REM poetry run coverage run manage.py test