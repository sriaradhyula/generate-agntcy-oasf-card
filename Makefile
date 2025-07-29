# Makefile for running a Python script with uv

# Variables
PYTHON_FILE = main.py
PORT = 10000

.PHONY: run
run:
	uv run $(PYTHON_FILE)
	@echo "Open your web browser and navigate to http://localhost:$(PORT)"