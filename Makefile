# define the name of the virtual environment directory
VENV := venv

TWINE_USERNAME ?= ""
TWINE_PASSWORD ?= ""

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

#run: venv
#	./$(VENV)/bin/python3 app.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

#.PHONY: all venv run clean

test: venv
	PYTHONPATH="." pytest ./tests

publish:
	TWINE_USERNAME=$(TWINE_USERNAME) TWINE_PASSWORD=$(TWINE_PASSWORD) twine upload dist/*