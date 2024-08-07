test:
	poetry run tox

cov:
	poetry run coverage report -m

cov-xml:
	poetry run coverage xml