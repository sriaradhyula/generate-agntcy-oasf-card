# Makefile for running a Python script with uvicorn and serving a static website

# Variables
PYTHON_FILE = main.py
HOST = 127.0.0.1
PORT = 8000
STATIC_DIR = static

.PHONY: run
run:
	uvicorn $(PYTHON_FILE):app --host $(HOST) --port $(PORT) --reload

.PHONY: serve-static
serve-static:
	python3 -m http.server --directory $(STATIC_DIR) $(PORT)

.PHONY: clean
clean:
	@echo "Nothing to clean for now."