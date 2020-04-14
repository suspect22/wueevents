FROM python:3.6
MAINTAINER suspect22

ENV PYTHONUNBUFFERED 1
ENV PYTHONUSER pythonenvuser
ENV WORKDIR /pythonenv

COPY ./requirements.txt /pythonenv/requirements.txt
RUN pip install -r /pythonenv/requirements.txt

WORKDIR ${WORKDIR}
COPY ./wueevents ${WORKDIR}
RUN adduser ${PYTHONUSER} --disabled-password --gecos "" && \
    chown ${PYTHONUSER}.$PYTHONUSER ${WORKDIR} && \
    chmod 755 ${WORKDIR}


USER ${PYTHONUSER}

EXPOSE 8000/udp
EXPOSE 8000/tcp
COPY . /pythonenv
ENTRYPOINT python /pythonenv/wueevents/manage.py runserver 0.0.0.0:8000