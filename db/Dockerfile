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
# CMD ["mysql", "-u", "root", "-p"]
# CMD ["password"]
# CMD ["source", "init.sql"]
# CMD mysql -u $MYSQL_USER -p $MYSQL_PASSWORD $MYSQL_DATABASE

# To build (in this working dir):
# sudo docker build -t [PICK_CONTAINER_NAME] .

# To run:
# sudo docker run --name [CONTAINER_NAME] -e MYSQL_ROOT_PASSWORD=password -d [IMAGE_NAME]

# To access:
# sudo docker exec -it [CONTAINER_NAME] bash
