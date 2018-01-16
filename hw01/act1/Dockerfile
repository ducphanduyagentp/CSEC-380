# Dockerfile for apache webserver

# Based on ubuntu 16.04 LTS
FROM ubuntu:xenial

RUN apt-get -y update && apt-get -y install apache2

COPY index.html /var/www/html/

EXPOSE 80

ENTRYPOINT service apache2 start

