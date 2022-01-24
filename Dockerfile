ARG TEMP_DIR=temp

FROM python:3.9-slim-buster as builder
ARG TEMP_DIR
SHELL ["/bin/bash", "-c"]
WORKDIR /$TEMP_DIR

RUN apt-get update \
    && apt-get install -y \
    gcc \
    && mkdir "/$TEMP_DIR/deb" \
    && apt-get install -y --no-install-recommends -o Dir::Cache::Archives="/$TEMP_DIR/deb" libpq-dev \
    && pip install poetry

COPY ./pyproject.toml ./poetry.lock* ./

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --dev \
    && pip wheel --no-cache-dir --no-deps --wheel-dir ./wheels -r requirements.txt

FROM python:3.9-slim-buster
SHELL ["/bin/bash", "-c"]
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG TEMP_DIR
WORKDIR /app

COPY --from=builder /$TEMP_DIR/deb/*.deb ./deb/
RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/* \
    && dpkg -i ./deb/*.deb

RUN addgroup --system app && adduser --system --group app
USER app
ENV PATH="/home/app/.local/bin:${PATH}"

COPY ./entrypoint.sh ./alembic.ini ./
COPY --from=builder /$TEMP_DIR/wheels/ ./wheels
COPY --from=builder /$TEMP_DIR/requirements.txt ./requirements.txt

RUN pip install --no-cache ./wheels/*
COPY ./tests ./tests
COPY ./fastapi_sandbox ./fastapi_sandbox

ENTRYPOINT ["/app/entrypoint.sh"]
