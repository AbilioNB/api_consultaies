FROM ubuntu:20.04
#FROM python:3.8

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update; apt -y update
RUN apt-get -y upgrade; apt -y upgrade
RUN apt-get install -y apt-utils wget
RUN apt-get install net-tools
RUN apt-get install nano
RUN apt-get -y update
RUN apt-get install -y git python3 vim 

RUN apt install -y python3-pip
RUN pip3 install virtualenv



WORKDIR /home

RUN git clone https://github.com/AbilioNB/api_consultaies
WORKDIR /home/api_consultaies
RUN pip install -r requirements.txt
WORKDIR /home/api_consultaies/restapi
EXPOSE 8000
CMD ["python3", "manage.py", "runserver"]
#RUN python3 manage.py runserver