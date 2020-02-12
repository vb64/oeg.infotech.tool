.PHONY: all setup exe
# make tests >debug.log 2>&1

ifeq ($(OS),Windows_NT)
PYTHON = venv\Scripts\python.exe
PYINSTALLER = venv\Scripts\pyinstaller.exe
PTEST = venv/Scripts/pytest.exe
COVERAGE = venv/Scripts/coverage.exe
else
PYTHON = ./venv/bin/python
PYINSTALLER = ./venv/bin/pyinstaller
PTEST = ./venv/bin/pytest
COVERAGE = ./venv/bin/coverage
endif

SOURCE = source
TESTS = tests
PYTEST = $(PTEST) --cov=$(SOURCE) --cov-report term:skip-covered

all: tests

test:
	$(PYTEST) -s --cov-append $(TESTS)/test/$(T)
	$(COVERAGE) html --skip-covered

tests: flake8 lint
	$(PYTEST) --durations=5 $(TESTS)
	$(COVERAGE) html --skip-covered

flake8:
	$(PYTHON) -m flake8 --max-line-length=120 $(TESTS)
	$(PYTHON) -m flake8 --max-line-length=120 $(SOURCE)

lint:
	$(PYTHON) -m pylint $(TESTS)/test
	$(PYTHON) -m pylint $(SOURCE)

exe: tests
	$(PYINSTALLER) --onefile $(SOURCE)/infotech.py

setup: setup_python setup_pip

setup_pip:
	$(PYTHON) -m pip install -r requirements.txt
	$(PYTHON) -m pip install -r tests/requirements.txt

setup_python:
	$(PYTHON_BIN) -m virtualenv ./venv
