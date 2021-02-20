#!/bin/sh

runtest=${RUNTEST:-"no"}

if [ "$runtest" = "yes" ]; then
  pytest -s -v --disable-pytest-warnings core/tests.py
 else
  python main.py
fi