FROM registry.centos.org/centos/centos:7
MAINTAINER Fridolin Pokorny <fridolin@redhat.com>

ENV LANG=en_US.UTF-8

RUN useradd api

RUN yum install -y epel-release && \
    yum install -y python34-devel python34-pip gcc && \
    yum clean all

COPY ./ /tmp/tmp_api_install/
RUN pushd /tmp/tmp_api_install &&\
  pip3 install . &&\
  popd &&\
  rm -rf /tmp/tmp_api_install

COPY hack/run_api.sh /usr/bin/

USER api
CMD ["/usr/bin/run_api.sh"]
