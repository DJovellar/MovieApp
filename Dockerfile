# base image 
FROM python:3.7.2

# File Author / Maintainer
MAINTAINER MovieApp

# Copy the application folder inside the container
ADD . /usr/src/app

# set the default directory where CMD will execute
WORKDIR /usr/src/app

COPY requirements.txt ./

# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 8000

CMD exec gunicorn MovieApp.wsgi:application --bind 0.0.0.0:8000 --workers 3
