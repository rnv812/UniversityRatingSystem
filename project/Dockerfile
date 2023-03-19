FROM python:3.11-alpine as builder

ARG DEPLOY_ENV=dev

ENV DEPLOY_ENV=${DEPLOY_ENV} \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.4.0

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install "poetry==$POETRY_VERSION" && \
    poetry config virtualenvs.in-project true && \
    poetry install $(test $DEPLOY_ENV = prod && echo "--without dev") --no-root --no-interaction --no-ansi


FROM base as final

WORKDIR /app

COPY . /app
COPY --from=builder /app/.venv ./.venv

RUN addgroup -g 1000 app && \
    adduser app -h /app -u 1000 -G 1000 -DH

USER app

ENTRYPOINT ["./entrypoint.sh"]
