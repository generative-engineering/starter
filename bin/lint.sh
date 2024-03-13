#!/usr/bin/env sh
# Any failure is bad
set -eu

cd "$(dirname "$0")/.."


export GREY='\033[0;37m'
export GREEN='\033[0;32m'
export RED='\033[0;31m'
export BOLD='\033[0;1m'
export BOLD_GREEN='\e[1;32m'
export NO_COLOUR='\033[0m'

fatal() {
  printf "${RED}FATAL: ${NO_COLOUR}%s\n" "$*" >/dev/stderr
  exit 2
}

# Configure Ruff options
args="$*"
formatOpts=""
lintOpts="--fix --show-fixes"
if [ "$args" = "--check" ] ; then
  printf "${GREY}%s${NO_COLOUR}\n" "Running check only"
  formatOpts="--check"
  lintOpts=""
elif [ -n "$args" ]; then
  fatal "Don't understand args '$args'. Try --check"
fi


running() {
   printf "${GREY}Running %s${NO_COLOUR}...\n" "$*"
}

success() {
    printf "${BOLD_GREEN}%79s${NO_COLOUR}\n" "✔ $*"
}

run() {
    name=$1
    running "$name"
    shift
    cmd="$*"
    $cmd
    success "$name"
}

# Run all the linting in a sensible order
run "Poetry checks" poetry check
run "Ruff format" ruff format "$formatOpts" src tests
run "Ruff lint" ruff check "$lintOpts" src tests
run "MyPy" mypy
