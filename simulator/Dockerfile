FROM ubuntu:20.04

WORKDIR /app
RUN apt-get update -y && \
	apt-get upgrade -y &&\
	apt-get install -y libxml2-dev && \
	apt-get install -y libssl-dev && \
	apt-get install -y libsasl2-dev && \
	apt-get install -y libcurl4-openssl-dev

RUN apt-get install python3-pip -y

RUN pip3 install pandas
RUN pip3 install requests

COPY controlRoom.py data_sensors.pkl ./

CMD python3 controlRoom.py


