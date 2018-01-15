FROM fedora:27

ENV LANG=en_US.UTF-8

RUN useradd api

RUN dnf install -y python3-pip && dnf clean all

COPY ./ /tmp/tmp_api_install/
# TODO: Move git+ installation to requirements once published to PyPI.
RUN pushd /tmp/tmp_api_install &&\
  pip3 install . &&\
  pip3 install gunicorn &&\
  popd &&\
  rm -rf /tmp/tmp_api_install &&\
  dnf install -y git &&\
  pip3 install git+https://github.com/fridex/thoth-pkgdeps@master

COPY hack/run_api.sh /usr/bin/

#USER api
CMD ["/usr/bin/run_api.sh"]
