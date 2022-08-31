FROM ubuntu:20.04 AS base

# RUN apt-get update -y
# RUN apt-get install -y python3
# RUN apt-get install -y python3-pip

# Environmental variables
ARG RUN_ENV=default
ENV RUN_ENV $RUN_ENV
RUN echo $RUN_ENV
 
# COPY . .