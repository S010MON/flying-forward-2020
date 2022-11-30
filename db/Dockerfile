# Filename: Database

# Base Image
FROM mysql:latest

# Update
RUN apt-get -y update
RUN apt-get -y install vim nano

# Setup SQL environment
ENV MYSQL_USER: root
ENV MYSQL_PASSWORD: password
ENV MYSQL_ROOT_PASSWORD: password
ENV MYSQL_DATABASE: droneData

EXPOSE 3306

ADD . .
WORKDIR .
