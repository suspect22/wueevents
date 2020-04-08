FROM python:3
MAINTAINER suspect22

#
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /pythonenv/requirements.txt
RUN pip install -r /pythonenv/requirements.txt

WORKDIR /pythonenv
COPY ./wueevents /pythonenv

RUN adduser -q pythonenvuser
USER PythonEnvUser

EXPOSE 8000/udp
EXPOSE 8000/tcp
COPY . /pythonenv
ENTRYPOINT python /pythonenv/wueevents/manage.py runserver 0.0.0.0:8000