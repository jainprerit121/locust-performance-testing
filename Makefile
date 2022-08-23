# Makefile

venv:
	test -d venv || python3 -m venv venv

freeze:
	pip freeze > requirements.txt

install: venv
	. venv/bin/activate && pip install -r requirements.txt

clean:
	find . -name 'venv' -type d | xargs rm -fr
	find . -name '__pycache__' -type d | xargs rm -fr
	find . -name '*.egg-info' -type d | xargs rm -fr
	find . -name '*.pyc' -delete
	find . -name '.coverage' -delete
	find . -name '*.pytest_cache' -type d | xargs rm -fr
	find . -name '*.mypy_cache' -type d | xargs rm -fr