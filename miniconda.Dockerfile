FROM ubuntu:22.04

WORKDIR /app

# base packages, which might be useful
RUN apt update && apt -y upgrade \
  && apt install -y --no-install-recommends \
    wget \
    ca-certificates \
    g++ \
    git \
    && rm -rf /var/lib/apt/lists/*
RUN apt update
RUN apt install libgl1-mesa-glx -y
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN mkdir /root/.conda
RUN bash Miniconda3-latest-Linux-x86_64.sh -b
RUN rm -f Miniconda3-latest-Linux-x86_64.sh