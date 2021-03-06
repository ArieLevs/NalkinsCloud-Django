
FROM python:3.7-alpine

MAINTAINER Arie Lev

ENV PYTHONUNBUFFERED 1
ARG PYPI_REPO="https://pypi.python.org/simple"
ENV PYPI_REPO $PYPI_REPO

RUN mkdir /nalkinscloud-api
WORKDIR /nalkinscloud-api

# Needed for mysqlclient requirement when using python alpine image
RUN apk add --no-cache mariadb-dev build-base libffi-dev

ADD src /nalkinscloud-api
RUN pip install \
    --index-url $PYPI_REPO \
    --requirement requirements.txt

# Cleanup
ENV PYPI_REPO 'None'

ADD entrypoint.sh /nalkinscloud-api
RUN chmod +x entrypoint.sh

RUN chmod 755 -R /nalkinscloud-api

ENTRYPOINT ["sh", "/nalkinscloud-api/entrypoint.sh"]
