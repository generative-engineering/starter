run: ## Run explorer for a given design file. To add arguments to the target, use '--' flag to separate from Make's
	@echo "Run explorer with '$(filter-out $@,$(MAKECMDGOALS))' ..."
	@poetry run explorer run --fabric src $(filter-out $@,$(MAKECMDGOALS)) $(ARGS) --log-level "INFO"

test: ## Test fabric function and components
	@poetry run pytest

clean: ## Clean output folder
	@echo "Cleaning output folder..."
	@rm -rf ./output/**

lint: ## Run linter on ./src and ./tests
	@./bin/lint.sh

design_files: ## Test design files by compiling them
	@echo "Compiling design files to test validity ..."
	@for f in designs/*.yaml; do poetry run explorer compile --fabric src $$f; done

help: ## See a list of all available targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.* ?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'


.PHONY: all $(MAKECMDGOALS)

.DEFAULT_GOAL := help


