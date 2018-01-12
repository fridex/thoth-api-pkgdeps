#!/usr/bin/python3

import os
from setuptools import setup, find_packages


def get_requirements():
    requirements_txt = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
    with open(requirements_txt) as fd:
        return fd.read().splitlines()


setup(
    name='thoth-api-pkgdeps',
    version='0.0.1',
    packages=find_packages(),
    package_data={
        'thoth_api_pkgdeps': [
            'swagger.yaml'
        ]
    },
    scripts=[os.path.join('thoth_api_pkgdeps', 'entrypoint.py')],
    install_requires=get_requirements(),
    include_package_data=True,
    author='Fridolin Pokorny',
    author_email='fridolin@redhat.com',
    maintainer='Fridolin Pokorny',
    maintainer_email='fridolin@redhat.com',
    description='Thoth API for pkgdeps',
    license='ASL 2.0',
    keywords='thoth packages API',
    url='https://github.com/fridex/thoth-api-pkgdeps',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Intended Audience :: Developers",
    ]
)
