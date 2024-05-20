lint:
	poetry run isort prometheus_demo/
	poetry run black prometheus_demo/
	poetry run pyright prometheus_demo/
	poetry run pyflakes prometheus_demo/

install:
	poetry install

run:
	poetry run prometheus-demo
