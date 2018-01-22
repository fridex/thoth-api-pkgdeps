FROM fedora:27
CMD ["/usr/bin/run_api.sh"]
ENTRYPOINT ["/usr/bin/run_api.sh"]
EXPOSE 34000
ENV \
 LANG=en_US.UTF-8 \
 GOPATH='/tmp/go' \
 APP_SERVICE_PORT=34000

RUN \
 useradd api &&\
 dnf install -y python3-pip git &&\
 dnf clean all

COPY ./ /tmp/tmp_api_install/
# TODO: Move git installation to requirements once published to PyPI.
RUN \
 pushd /tmp/tmp_api_install &&\
 pip3 install . &&\
 pip3 install gunicorn &&\
 git clone https://github.com/fridex/thoth-pkgdeps &&\
 cd thoth-pkgdeps &&\
 sh hack/install_rpm.sh &&\
 make &&\
 pip3 install . &&\
 popd &&\
 dnf clean all &&\
 rm -rf /tmp_api_install ${GOPATH} &&\
 unset GOPATH

COPY hack/run_api.sh /usr/bin/
USER api
