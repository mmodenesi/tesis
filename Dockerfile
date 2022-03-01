FROM ubuntu:21.10

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends texlive-full
RUN apt-get install -y --no-install-recommends python3-pip
RUN pip install Pygments
