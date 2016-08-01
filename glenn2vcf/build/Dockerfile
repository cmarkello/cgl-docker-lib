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

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 50
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 50

WORKDIR /home
RUN git clone --recursive https://github.com/adamnovak/glenn2vcf.git

WORKDIR /home/glenn2vcf
RUN git checkout 2bb4bc2cf161bd2a2ef6047750b79cdda6a6408c

RUN make
