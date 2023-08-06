.PHONY: test

test:
	python -m unittest discover -s tests -p '*_test.py'

lint:
	pylint --rcfile=.pylintrc game

lint-fix:
	black .
	pylint --rcfile=.pylintrc game