.PHONY: all test lint static fixtures migrate locale clean

all: test clean lint

test:
	mkdir -p reports; touch reports/coverage.xml; chmod -R 777 reports
	pytest ${APP}
	chmod -R 777 reports

lint:
	mkdir -p reports
	touch reports/bandit.json;
	touch reports/pylint.txt;
	chmod -R 777 reports/
	flake8
	isort -c --recursive
	bandit -s B101 -r -f json -o reports/bandit.json project_namer
	mypy project_name --txt-report reports
	pylint project_name | tee reports/pylint.txt
	chmod -R 777 reports

static:
	python3 manage.py collectstatic --noinput

fixtures:
	echo "add fixtures command"

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

locale:
	python3 manage.py makemessages --all
	python3 manage.py compilemessages

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	isort -y --recursive
	black project_name