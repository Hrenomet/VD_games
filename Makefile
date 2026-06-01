install:
	uv sync

VD-games:
	uv run VD-games

build:
	uv build

package-install:
	uv tool install dist/*.whl --force

clean:
	rm -rf .venv
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
