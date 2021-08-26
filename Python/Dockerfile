FROM python:3.8.3-alpine

WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./project/requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

# copy project file
COPY ./project /usr/src/app

# the container is listening on port 8000
EXPOSE 8000

# migrate project
RUN python3 manage.py migrate