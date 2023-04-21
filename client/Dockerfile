FROM node:18-alpine as base

ARG DEPLOY_ENV

ENV DEPLOY_ENV=${DEPLOY_ENV}


FROM base as builder

WORKDIR /app/

COPY . /app/

RUN npm install


FROM base as final

COPY --from=builder /app/node_modules/ /app/node_modules/
COPY . ./app/

WORKDIR /app/

RUN chmod +x ./entrypoint.sh

RUN addgroup -S app && \
    adduser -S app -G app -h /app -DH

RUN mkdir .npm/ node_modules/.cache/ && \
    chown app:app -R .npm/ && \
    chown app:app -R node_modules/.cache/

USER app

ENTRYPOINT [ "./entrypoint.sh" ]
