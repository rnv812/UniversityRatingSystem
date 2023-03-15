FROM python:3.10-alpine as base

ARG DEPLOY_MODE

ENV DEPLOY_MODE ${DEPLOY_MODE} \
    PYTHONUNBUFFERED 1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random


FROM base as builder

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.4.0

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app
COPY . /app

RUN poetry config virtualenvs.in-project true && \
    poetry install $(test "$DEPLOY_MODE" == production && echo "--without dev") --no-root --no-interaction --no-ansi && \
    poetry build


FROM base as final

COPY --from=builder /app/.venv ./.venv
COPY --from=builder /app/dist .

RUN ./.venv/bin/pip install *.whl
