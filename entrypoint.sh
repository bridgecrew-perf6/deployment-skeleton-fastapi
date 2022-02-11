#!/bin/bash
alembic upgrade head

if [ "$DEBUG" = true ]
then
#    python -m fastapi_sandbox.main
    uvicorn fastapi_sandbox.main:app --host 0.0.0.0 --port 8000 --reload --debug
else
    uvicorn fastapi_sandbox.main:app --host 0.0.0.0 --port 8000
fi
