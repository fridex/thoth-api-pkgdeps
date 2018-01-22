#!/usr/bin/env python3

import logging

import requests

from thoth_pkgdeps import extract_buildlog
from thoth_pkgdeps import extract_image

from .configuration import Configuration

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


def api_extract_buildlog(build_log_info):
    build_log = build_log_info.get('buildlog')
    if not build_log:
        return {"error": "No data to be processed"}, 400

    result = extract_buildlog(build_log)
    return result, 200


def api_extract_image(image):
    # TODO: we will need to do this asynchronously as we can easily encounter timeouts.
    try:
        return extract_image(image, timeout=None)
    except Exception as exc:
        return {'error': str(exc)}, 400


def api_analyze(image, analyzer):
    # TODO: possibly timeout
    # TODO: refactor this so it is more generic
    endpoint = "{}/oapi/v1/namespaces/myproject/buildconfigs/" \
               "{}/webhooks/secret101/generic".format(Configuration.OPENSHIFT_API_URL, analyzer)
    payload = {'env': [{'name': 'IMAGE', 'value': image}]}
    response = requests.post(
        endpoint,
        headers={
            'Authorization': 'Bearer: {}'.format(Configuration.OPENSHIFT_API_TOKEN),
            'Content-Type': 'application/json'
        },
        json=payload,
        verify=False
    )
    response.raise_for_status()
    return {}, 202
