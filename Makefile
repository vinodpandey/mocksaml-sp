.PHONY: help check 

# Default goal
.DEFAULT_GOAL := help

help:
	@echo "Usage:"
	@echo "  make check"
	@echo "  "

check:
	isort apps
	black apps
	flake8 apps
	mypy apps --strict --follow-imports=skip 