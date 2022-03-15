ARG TEMP_DIR=opt/temp
ARG APT_CACHE_DIR=$TEMP_DIR/apt_cache
ARG WHEELS_DIR=$TEMP_DIR/wheels

FROM python:3.10-slim-buster as builder
ARG TEMP_DIR
ARG APT_CACHE_DIR
ARG WHEELS_DIR
SHELL ["/bin/bash", "-c"]

WORKDIR /$TEMP_DIR

RUN apt-get update \
    && apt-get install -y \
    gcc \
    && mkdir "/$APT_CACHE_DIR" \
    && apt-get install -y --no-install-recommends -o Dir::Cache::Archives="/$APT_CACHE_DIR" libpq-dev \
    && pip install poetry

COPY ./pyproject.toml ./poetry.lock* ./

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --dev \
    && pip wheel --no-cache-dir --no-deps --wheel-dir /$WHEELS_DIR -r requirements.txt

FROM python:3.10-slim-buster
ARG TEMP_DIR
ARG APT_CACHE_DIR
ARG WHEELS_DIR
SHELL ["/bin/bash", "-c"]

EXPOSE 8000

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG APP_DIR=opt/app
WORKDIR /$APP_DIR

COPY --from=builder /$APT_CACHE_DIR/*.deb /$APT_CACHE_DIR/
RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/* \
    && dpkg -i /$APT_CACHE_DIR/*.deb

COPY ./entrypoint.sh ./alembic.ini ./
RUN chmod +x ./entrypoint.sh

RUN addgroup --system app && adduser --system --group app
USER app
ENV PATH="/home/app/.local/bin:${PATH}"

COPY --from=builder /$WHEELS_DIR/ /$WHEELS_DIR
RUN pip install --no-cache /$WHEELS_DIR/*

COPY ./src .
