FROM python:3.9

RUN apt update && apt install -y \
    rpm \
    sudo \
    zsh \
    zsh-syntax-highlighting \
    zsh-doc 


ARG USERNAME=eosdev
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user
RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

RUN echo "eosdev ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    echo "# macros"                      >  /home/eosdev/.rpmmacros && \
    echo "%_topdir    /workspaces/dhcpv6-pd-route-sync/rpmbuild" >> /home/eosdev/.rpmmacros && \
    echo "%_sourcedir %{_topdir}/SOURCES"        >> /home/eosdev/.rpmmacros && \
    echo "%_builddir  %{_topdir}/BUILD"        >> /home/eosdev/.rpmmacros && \
    echo "%_specdir   %{_topdir}/SPECS"        >> /home/eosdev/.rpmmacros && \
    echo "%_rpmdir    %{_topdir}/RPM"        >> /home/eosdev/.rpmmacros && \
    echo "%_srcrpmdir %{_topdir}/SRPMS"        >> /home/eosdev/.rpmmacros && \
    mkdir /home/eosdev/rpmbuild && \
    chown -R eosdev /home/eosdev

RUN pip install jsonrpclib python2-secrets

#COPY .devcontainer/src/eossdk.py /usr/lib/python2.7/
COPY .devcontainer/src/eossdk.py /usr/lib/python3.9/site-packages/

USER eosdev

ENV name='DHCPv6PDRouteSync'

