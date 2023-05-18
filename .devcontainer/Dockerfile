FROM continuumio/anaconda3
ARG UID=1001
ARG GID=1001
ARG USERNAME=tokunaga
RUN groupadd -g ${GID} tokunaga
RUN useradd -u ${UID} -g ${GID} -s /bin/bash -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
RUN mkdir -p /opt/scrapy \
    && sudo chown -R ${UID}:${GID} /opt/scrapy

USER ${UID}
