############################################################
# Dockerfile to build Python App Container
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu

# File Author / Maintainer
MAINTAINER DaveSave

# Update the sources list
RUN apt-get update && apt-get install -y tar git curl wget dialog net-tools build-essential

# Install Python and Basic Python Tools
RUN apt-get install -y python python-dev python-distribute python-pip


# Install python modules and transfer code
RUN rm -rf /build
RUN mkdir /build
WORKDIR /build

ADD requirements.txt /build/
RUN pip install -r requirements.txt


RUN git clone https://github.com/davesave/usd_nis.git