.PHONY: help install venv test coverage lint format clean deploy

help:
    @echo "Common tasks:"
    @echo "  make install    - Set up venv and install dependencies"
    @echo "  make test       - Run all tests with pytest"
    @echo "  make coverage   - Run tests and show coverage report"
    @echo "  make lint       - Run flake8 for linting"
    @echo "  make format     - Format code with black"
    @echo "  make clean      - Remove Python cache and test artifacts"
    @echo "  make deploy     - Deploy the application (placeholder)"

venv:
    @test -d .venv || python3 -m venv .venv

install: venv
    . .venv/bin/activate; uv pip install -r requirements.txt

test:
    . .venv/bin/activate; pytest

coverage:
    . .venv/bin/activate; pytest --cov=.

lint:
    . .venv/bin/activate; flake8 .

format:
    . .venv/bin/activate; black .

clean:
    find . -type d -name "__pycache__" -exec rm -rf {} +
    rm -rf .pytest_cache .coverage htmlcov

deploy:
    @echo "Add deployment commands here (e.g., for Azure, Heroku, etc.)"