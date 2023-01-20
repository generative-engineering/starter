#!/usr/bin/env sh
set -e
cd "$(dirname "$0")/.."

fatal() {
  echo "FATAL: $*" >/dev/stderr
  exit 2
}

args="$*"
opts=""
if [ "$args" = "--check" ] ; then
  echo "Running check only"
  opts="--check"
elif [ -n "$args" ]; then
  fatal "Don't understand args: '$args'. Try --check"
fi

# Run all the linting in a sensible order
echo "Running isort..."
poetry run isort $opts src tests bin
echo "✓ isort completed successfully."

echo "Running black..."
poetry run black $opts src tests bin

echo "Running flake8..."
poetry run flake8 src tests bin
echo "✓ flake8 ran successfully."

echo "Running mypy..."
poetry run mypy
