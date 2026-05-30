install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl --force

VD-games:
	uv run VD-games
