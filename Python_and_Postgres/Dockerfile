FROM python:3.8.3-alpine

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip 
COPY ./project/requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project file
COPY ./project /usr/src/app

# the container is listening on port 8000
EXPOSE 8000
