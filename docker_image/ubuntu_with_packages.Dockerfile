FROM ubuntu:21.04


ENV TZ=US
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN sed -i "s/archive.ubuntu.com/old-releases.ubuntu.com/g" /etc/apt/sources.list
RUN sed -i "s/security.ubuntu.com/old-releases.ubuntu.com/g" /etc/apt/sources.list

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      curl \
      ca-certificates \
      gnupg \
      cpio \
      lsb-release \
      libpython3-dev \
      python-gi-dev \
      python3-minimal \
      python3-setuptools \
      python3-pip \
      net-tools \
      nmap \
      psmisc \
      sudo \
      bc \
      wget \
      build-essential \
      git \
      bison \
      flex \
      cmake \
      libtool \
      pkg-config \
      autoconf \
      dh-autoreconf \
      libzmq3-dev \
      tzdata && \
      rm -rf /var/lib/apt/lists/*

WORKDIR /working

RUN python3 -m pip install --upgrade pip && pip3 install tornado paho-mqtt