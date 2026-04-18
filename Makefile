PYTHON  := $(shell command -v python3 2>/dev/null || command -v python)
VENV    := .venv
VP      := $(VENV)/bin/python
PIP     := $(VENV)/bin/pip
PYTEST  := $(VENV)/bin/pytest

# ── Environment ────────────────────────────────────────────────────────────────

$(VENV): requirements-dev.txt requirements.txt pyproject.toml
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --quiet --upgrade pip
	$(PIP) install --quiet -r requirements-dev.txt
	@touch $(VENV)

.PHONY: install
install: $(VENV)  ## Create venv and install all dependencies

# ── Pipeline ───────────────────────────────────────────────────────────────────

.PHONY: fetch
fetch: $(VENV)  ## Fetch shared assets from open-circuits (idempotent)
	$(VP) build/fetch_shared.py

.PHONY: build
build: $(VENV)  ## Build the static HTML site into output/html/
	$(VP) build/build.py

.PHONY: all
all: fetch build  ## Fetch shared assets and build the site

.PHONY: serve
serve:  ## Serve output/html/ locally at http://localhost:8080
	cd output/html && python3 -m http.server 8080

# ── Tests ──────────────────────────────────────────────────────────────────────

.PHONY: test
test: $(VENV)  ## Run pytest
	@$(PYTEST); status=$$?; \
	if [ $$status -eq 5 ]; then \
		echo "No tests collected."; \
	elif [ $$status -ne 0 ]; then \
		exit $$status; \
	fi

# ── Housekeeping ───────────────────────────────────────────────────────────────

.PHONY: clean
clean:  ## Remove built output
	rm -rf output/html

.PHONY: clean-all
clean-all: clean  ## Remove output, venv, pytest cache, and shared assets
	rm -rf $(VENV) .pytest_cache shared/css shared/js shared/fonts shared/SHARED-VERSION.txt
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true

.PHONY: help
help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*##' $(MAKEFILE_LIST) \
	  | awk 'BEGIN {FS = ":.*##"}; {printf "  %-12s %s\n", $$1, $$2}'
