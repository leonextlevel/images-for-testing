FROM python:3.7-slim-buster

ARG APP_DIR
ARG PIPENV_ARGS

ENV APP_DIR=${APP_DIR}
ENV PIPENV_ARGS=${PIPENV_ARGS}

ENV WORK_DIR=/usr/src/app

RUN apt update && apt install libmagickwand-dev nginx -y

RUN pip install pipenv

COPY ./${APP_DIR}/ ${WORK_DIR}/${APP_DIR}
COPY ./migrations/ ${WORK_DIR}/migrations
COPY ./Pipfile ${WORK_DIR}
COPY ./Pipfile.lock ${WORK_DIR}

WORKDIR ${WORK_DIR}

RUN pipenv install --system

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 5000
