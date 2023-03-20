FROM python:3.11-alpine as base

ARG DEPLOY_ENV \
    APP_USER_UID

ENV PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VERSION=1.4.0


FROM base as builder

WORKDIR /app/

COPY pyproject.toml poetry.lock ./

RUN pip install poetry==$POETRY_VERSION && \
    poetry config virtualenvs.in-project true && \
    poetry install $(test $DEPLOY_ENV = prod && echo "--without dev") --no-root --no-interaction --no-ansi


FROM base as final

COPY . /app/src/
COPY --from=builder /app/.venv/ /app/.venv/

WORKDIR /app/src/

RUN addgroup -S app && \
    adduser -S app -G app -h /app -u $APP_USER_UID -DH

RUN chmod 775 ./entrypoint.sh
RUN chmod 775 ./activate.sh

USER app

ENTRYPOINT [ "./entrypoint.sh" ]