#!/usr/bin/env python3

import logging

from thoth_pkgdeps import extract_buildlog
from thoth_pkgdeps import extract_image


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
