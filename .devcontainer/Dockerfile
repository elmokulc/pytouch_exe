ARG BASE_IMAGE=mcr.microsoft.com/devcontainers/base:focal
FROM ${BASE_IMAGE}
LABEL "Elmo Chrisitian"="elmokulc@univ-smb.fr"

RUN chmod -R 777 /tmp
ENV DEBIAN_FRONTEND="noninteractive" TZ="Europe/London"
COPY ./_install_apt_packages.sh /tmp/_install_apt_packages.sh
RUN /bin/bash /tmp/_install_apt_packages.sh

COPY ./_install_softwares.sh /tmp/_install_softwares.sh
RUN /tmp/_install_softwares.sh


ARG CONDA_ENV_NAME=pytouch
ARG CONDA_DIR=/opt/conda

ENV CONDA_DIR=${CONDA_DIR}
ENV CONDA_ENV_NAME=${CONDA_ENV_NAME}
ENV CONDA_ENV_PATH=${CONDA_DIR}/envs/${CONDA_ENV_NAME}
ENV CONDA_ENV_BIN_PATH=${CONDA_ENV_PATH}/bin
ENV CONDA_BIN_PATH=/opt/conda/bin/conda
ENV MAMBA_BIN_PATH=/opt/conda/bin/mamba
ENV PYTHON_EXECUTABLE=${CONDA_ENV_BIN_PATH}/python

COPY ./_install_miniforge.sh /tmp/_install_miniforge.sh
RUN chmod +x /tmp/_install_miniforge.sh && /tmp/_install_miniforge.sh


RUN ${MAMBA_BIN_PATH} create -y -n ${CONDA_ENV_NAME}
COPY environment.yml /tmp/environment.yml
RUN umask 0000 && ${MAMBA_BIN_PATH} update -n base -c conda-forge conda 
RUN umask 0000 && ${MAMBA_BIN_PATH} env update --file /tmp/environment.yml --name ${CONDA_ENV_NAME}

# INSTALL ARAVIS
RUN echo "** Installing Aravis"
RUN $CONDA_ENV_BIN_PATH"/pip" install PyGObject
RUN ${MAMBA_BIN_PATH} install -y libusb gtk3 gtk3-tests -n pytouch

RUN echo "** Downloading Aravis 0.8.31"
RUN umask 000 && \
    mkdir aravis && \
    cd /aravis && \
    wget https://github.com/AravisProject/aravis/releases/download/0.8.31/aravis-0.8.31.tar.xz && \
    tar -xf aravis-0.8.31.tar.xz && \
    cd aravis-0.8.31

RUN echo "** Meson building"
# RUN export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/lib/x86_64-linux-gnu/pkgconfig && \
#     mkdir -p /usr/lib/bin && \
#     ln -s /opt/conda/envs/pytouch/bin/* /usr/lib/bin/ && \
RUN export PATH=$CONDA_ENV_BIN_PATH:$PATH && \
    umask 000 && \
    cd /aravis/aravis-0.8.31 && \
    $CONDA_ENV_BIN_PATH"/meson" build && \
    cd build && \
    $CONDA_ENV_BIN_PATH"/meson" configure -Dprefix=$CONDA_ENV_PATH \
    -Dlibdir=lib \
    -Dcmake_prefix_path=/usr/lib/x86_64-linux-gnu/pkgconfig \
    -Dpkgconfig.relocatable=true \
    -Dintrospection=enabled \
    -Dusb=enabled \
    -Dviewer=enabled \
    -Dpacket-socket=enabled \
    -Dgst-plugin=enabled \
    -Dfast-heartbeat=true && \
    cd ..

RUN umask 000 && \
    export PATH=$CONDA_ENV_BIN_PATH:$PATH && \
    cd /aravis/aravis-0.8.31/build && \
    $CONDA_ENV_BIN_PATH"/ninja" && \
    $CONDA_ENV_BIN_PATH"/ninja" install && \
    ldconfig

ENV GI_TYPELIB_PATH="/aravis/aravis-0.8.31/build/src"
ENV LD_LIBRARY_PATH="/aravis/aravis-0.8.31/build/src/.libs"
RUN ldconfig

RUN echo "**Install python-aravis"
RUN umask 000 && \
    cd /aravis/aravis-0.8.31/ && \
    git clone https://github.com/SintefManufacturing/python-aravis && \
    cd python-aravis && \
    umask 000 && \
    $CONDA_ENV_BIN_PATH"/python" setup.py install && \
    ldconfig && \
    echo "** python-aravis successfully installed"

COPY aravis.rules /etc/udev/rules.d
 
RUN echo "ulimit -c 0" >> /home/vscode/.bashrc
RUN echo ". /opt/conda/etc/profile.d/conda.sh" >> /home/vscode/.bashrc
RUN echo "conda activate $CONDA_ENV_NAME" >> /home/vscode/.bashrc
 
RUN usermod -a -G video vscode
RUN usermod -a -G root vscode 
RUN usermod -a -G dialout vscode

# Copy the devcontainer script
COPY postCreateCommand.sh /tmp/postCreateCommand.sh
COPY postStartCommand.sh /tmp/postStartCommand.sh

