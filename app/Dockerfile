FROM ubuntu:20.04

WORKDIR /app
RUN apt-get update -y && \
	apt-get upgrade -y &&\
	apt-get install -y libxml2-dev && \
	apt-get install -y libssl-dev && \
	apt-get install -y libsasl2-dev && \
	apt-get install -y libcurl4-openssl-dev

RUN apt-get install python3-pip -y

COPY ./dependencies.txt .
RUN pip3 install -r dependencies.txt

RUN apt-get install -y uvicorn

COPY database ./database
COPY model ./model

COPY main.py config.py ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 


