# base image
FROM python:3.10
# setup environment variable
ENV DockerHOME=/code \
    POETRY_VERSION=1.1.14


# set work directory
RUN mkdir -p $DockerHOME

# where your code lives
WORKDIR $DockerHOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_CACHE_DIR='/var/cache/pypoetry'

# install dependencies
RUN pip install --upgrade pip &&  \
    pip install "poetry==$POETRY_VERSION" && poetry --version

COPY requirements.txt /code/


RUN pip install -r requirements.txt
# copy whole project to your docker home directory.
COPY . $DockerHOME
# run this command to install all dependencies


# port where the Django app runs
EXPOSE 8000
# start server

CMD python manage.py runserver