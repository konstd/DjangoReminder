#!/usr/bin/env bash

cd service/

if [ -z "$VIRTUAL_ENV" ]; then
  VIRTUAL_ENV="../../.venv/"
fi

EXIT_CODE=$(${VIRTUAL_ENV}/bin/python -m manage makemigrations --dry-run 2>&1 | grep "No changes detected" | wc -l)
if [ $EXIT_CODE != 1 ]; then
  ${VIRTUAL_ENV}/bin/python -m manage makemigrations --dry-run
  exit 1
fi
