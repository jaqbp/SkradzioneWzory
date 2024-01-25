format:
	ruff format . --no-cache

lint:
	ruff check . --no-cache

clean-cache:
	find . \( \
		-type d -name .pytest_cache -o -type d -name __pycache__ -o -name "*.pyc" -o -type d -name .mypy_cache \
	\) -prune -exec rm -rf {} \;
