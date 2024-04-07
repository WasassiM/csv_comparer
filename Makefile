format:
	poetry run black .

test:
	poetry run pytest .

test_csv_file:
	poetry run pytest ./tests/test_csv.py

test_compare:
	poetry run pytest ./tests/test_compare.py

test_coverage:
	poetry run pytest --cov=csv_compare --cov-report=html

build:
	poetry build

publish:
	poetry publish