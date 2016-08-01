FROM ubuntu:16.04

MAINTAINER Charles Markello, cmarkell@ucsc.edu

RUN apt-get update \
    && apt-get install -y \
    gcc-4.9 \
    g++-4.9 \
    git \
    make \
    protobuf-compiler \
    libprotoc-dev \
    libjansson-dev \
    libbz2-dev \
    libncurses5-dev \
    automake libtool jq samtools curl unzip redland-utils \
    librdf-dev cmake pkg-config wget bc gtk-doc-tools raptor2-utils rasqal-utils bison flex

RUN mkdir /opt/glenn2vcf/

COPY glenn2vcf /usr/local/bin/
COPY wrapper.sh /opt/glenn2vcf/

RUN mkdir /data
WORKDIR /data

ENTRYPOINT ["sh", "/opt/glenn2vcf/wrapper.sh"]
