FROM python:3.8.3-alpine

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk add --no-cache make build-base
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip 
COPY ./python/requirements.txt /usr/src/app
RUN pip install -r requirements.txt

# copy project file
COPY ./python /usr/src/app

RUN python manage.py makemigrations image_test
RUN python manage.py migrate
RUN python manage.py collectstatic    
