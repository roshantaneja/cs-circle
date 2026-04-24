#!/usr/bin/env bash
# check.sh — run a student's homework against the test suite.
#
# Usage:
#   ./check.sh priansh            # runs tests against the priansh/ folder on the current branch
#   ./check.sh devarshi
#   ./check.sh priansh --branch   # fetches & checks out priansh's branch first, then runs tests
#
# Exits non-zero if the tests fail.
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <devarshi|priansh> [--branch]" >&2
  exit 2
fi

STUDENT="$1"
shift || true

if [[ "$STUDENT" != "devarshi" && "$STUDENT" != "priansh" ]]; then
  echo "error: student must be 'devarshi' or 'priansh' (got '$STUDENT')" >&2
  exit 2
fi

if [[ "${1-}" == "--branch" ]]; then
  echo ">>> fetching origin/$STUDENT"
  git fetch origin "$STUDENT"
  echo ">>> checking out $STUDENT"
  git checkout "$STUDENT"
  git pull origin "$STUDENT"
fi

echo ">>> running tests for STUDENT=$STUDENT"
STUDENT="$STUDENT" python -m pytest tests/ -v
