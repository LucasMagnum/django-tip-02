clean: ## Clean environment
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -f *.log

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

setup: setup-tests  ## Install dependencies

setup-tests:  ## Install python requirements
	pip install -r requirements.txt

tests: clean lint ## Run tests
	cd app & python app/manage.py test products -v2

lint:  ## Lint project
	flake8
