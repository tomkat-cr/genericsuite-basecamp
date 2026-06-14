# File: exampleapp_backend/Dockerfile
# 2022-02-25 | CR

FROM python:3.11

ARG FLASK_APP=chalicelib
ARG APP_STAGE=dev
ARG APP_DEBUG=0
ARG APP_DB_NAME=exampleapp_dev
ARG APP_DB_URI
ARG APP_SECRET_KEY

# Create app directory
WORKDIR /usr/src/app
 
COPY . .

# RUN ls -la

RUN sh -x ./scripts/docker_install_deps.sh
# RUN mkdir ./logs
# RUN echo "" > ./logs/app_general.log
RUN pipenv install --deploy --system

EXPOSE 5000

CMD [ "bash", "scripts/run_server.sh" ]

