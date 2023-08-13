.PHONY: test

test:
	coverage run -m unittest discover -s tests -p '*_test.py'
	coverage report -m 
	coverage html

lint:
	pylint --rcfile=.pylintrc game

lint-fix:
	black .
	pylint --rcfile=.pylintrc game