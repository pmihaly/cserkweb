FROM python:3.7

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv install --ignore-pipfile --system --deploy

COPY . .