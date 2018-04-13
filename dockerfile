FROM ubuntu:latest
RUN apt-get update && apt-get install -y curl
RUN curl -LO https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -p /miniconda -b
RUN rm Miniconda3-latest-Linux-x86_64.sh
ENV PATH=/miniconda/bin:${PATH}
RUN conda update -y conda

# Python packages from conda
# RUN conda install -y \
#     scikit-image \
#     flask \
#     pillow

WORKDIR /tmp
