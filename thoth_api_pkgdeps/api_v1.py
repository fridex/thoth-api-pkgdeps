#!/usr/bin/env python3

import logging


_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)


def hello():
    _LOGGER.info("Hello!")
    return {"message": "Hello world!"}, 200

