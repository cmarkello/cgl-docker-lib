FROM ubuntu:16.04

MAINTAINER Charles Markello, cmarkell@ucsc.edu

RUN apt-get update \
	&& apt-get install -y \
	build-essential \
	git \
	python-dev
	
RUN pip install --upgrade pip
RUN pip install 

RUN mkdir /data
RUN git clone https://github.com/vgteam/vg.git /opt/chunked_call
RUN cd /opt/chunked_call && git checkout 5415525e3fbc95542c526141da72f92561845a4b

COPY wrapper.sh /opt/chunked_call/scripts/
WORKDIR /data

ENTRYPOINT ["sh", "/opt/chunked_call/wrapper.sh"]
