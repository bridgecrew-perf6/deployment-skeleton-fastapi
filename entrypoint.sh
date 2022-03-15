#!/bin/bash
if [ "$DEBUG" = true ]
then
    alembic upgrade head
#    python -m fastapi_sandbox.main
    uvicorn fastapi_sandbox.main:app --host 0.0.0.0 --port 8000 --reload --debug
else
    uvicorn fastapi_sandbox.main:app --host 0.0.0.0 --port 8000
fi
