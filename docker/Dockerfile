############################################################
# Dockerfile to build Python App Container
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu:13.10

MAINTAINER Dave

# Update the sources list
RUN apt-get update && apt-get install -y python3 python3-pip tar git build-essential

VOLUME        ["/export"]
RUN ls -l /export
CMD ls -l /export

# Install python modules and transfer code
RUN rm -rf /build
RUN mkdir /build
WORKDIR /build

ADD requirements.txt /build/
RUN pip3 install -r requirements.txt


RUN git clone https://github.com/davesave/usd_nis.git

#CMD python /build/usd_nis.py
CMD python3 /build/usd_nis/usd_nis.py >> /export/test
