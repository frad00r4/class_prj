FROM python:2.7
MAINTAINER Andrey Kochnev <frad00r4@gmail.com>
EXPOSE 8000

WORKDIR /opt/build

COPY ./requirements.txt /opt/build

RUN pip install -r /opt/build/requirements.txt
RUN pip install uwsgi

ENTRYPOINT ["/bin/bash", "/opt/class_project/entrypoint.sh"]
