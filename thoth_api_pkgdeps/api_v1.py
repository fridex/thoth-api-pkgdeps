#!/usr/bin/env python3

import logging

from thoth_pkgdeps import extract_build_log


_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


def api_extract_build_log(build_log_info):
    build_log = build_log_info.get('buildlog')
    if not build_log:
        return {"error": "No data to be processed"}, 400

    result = extract_build_log(build_log)
    return result, 200
