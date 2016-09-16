FROM quay.io/ucsc_cgl/toil:3.5.0a1--629bfbdf1eb01ed9f68f997671fbae3e76d5c3de
#FROM quay.io/ucsc_cgl/toil-it:3.5.0a1--d426c85934fc0791818d701ea3e694cecb8afc17
#FROM ubuntu:14.04

# File Author / Maintainer
MAINTAINER Charles Markello <cmarkell@ucsc.edu>

RUN apt-get update && apt-get install -y \
    git \
    python-dev \
    python-pip \
    wget \
    curl \
    apt-transport-https \
    ca-certificates

# The stock pip is too old and can't install from sdist with extras
RUN pip install --upgrade pip

## Install dateutil
#RUN pip install python-dateutil

#RUN python -c "import sys; print '\n'.join(sys.path)"
#RUN python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"
#RUN python -c "import dateutil; print(dateutil.__path__)"

## Move dateutil module onto the python path
#RUN ln -s /usr/local/lib/python2.7/dist-packages/dateutil /usr/lib/python2.7/dist-packages/dateutil

RUN pip list

## Get the Docker binary
#RUN wget https://get.docker.com/builds/Linux/x86_64/docker-DOCKERVER -O /usr/local/bin/docker
#RUN chmod u+x /usr/local/bin/docker

## Install Toil
#RUN pip install toil[mesos,aws,azure]==3.4.0a1.dev228

# Install toil-lib
RUN git clone --recursive https://github.com/cmarkello/toil-lib.git
RUN pip install ./toil-lib

# Install toil-scripts
RUN git clone --recursive https://github.com/cmarkello/toil-scripts.git
WORKDIR ./toil-scripts
RUN git fetch
RUN git checkout -b vg_evaluation_pipeline origin/vg_evaluation_pipeline
WORKDIR ../
RUN pip install ./toil-scripts

RUN pip list

COPY wrapper.sh /opt/vg-pipeline/

ENTRYPOINT ["sh", "/opt/vg-pipeline/wrapper.sh"]
