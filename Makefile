VENV:=$(CURDIR)/.venv
VBIN:=$(VENV)/bin
ACTIVATE:=$(VBIN)/activate
PIP:=$(VBIN)/pip
PYTHON:=$(VBIN)/python

.PHONY: venv install

venv: $(ACTIVATE)

$(VENV):
	@virtualenv -p python3.6 --no-site-packages $(VENV)

$(ACTIVATE): requirements.txt $(VENV)
	@$(PIP) install -Ur requirements.txt
	@touch $(ACTIVATE)

install: $(ACTIVATE)
	@$(PIP) install -U .
