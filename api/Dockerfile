FROM python:3.11-alpine as base

ARG DEPLOY_ENV

ENV DEPLOY_ENV=${DEPLOY_ENV} \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.4.0


FROM base as builder

WORKDIR /app/

COPY src/pyproject.toml src/poetry.lock ./

RUN pip install poetry==$POETRY_VERSION && \
    poetry config virtualenvs.in-project true && \
    poetry install $(test $DEPLOY_ENV = prod && echo "--without dev") --no-root --no-interaction --no-ansi



FROM base as composer

COPY --from=builder /app/.venv/ /app/.venv/
COPY src/ /app/src/

WORKDIR /app/src/

RUN rm pyproject.toml poetry.lock


FROM base as final

COPY --from=composer /app/ /app/

WORKDIR /app/src/

RUN chmod +x ./entrypoint.sh && \
    chmod +x ./activate.sh && \
    chmod +x ./load-fixture.sh

RUN addgroup -S app && \
    adduser -S app -G app -h /app -DH

USER app

ENTRYPOINT [ "./entrypoint.sh" ]
