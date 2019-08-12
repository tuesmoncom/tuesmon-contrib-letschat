#!/usr/bin/env python
# -*- coding: utf-8 -*-

import versiontools_support
from setuptools import setup, find_packages

setup(
    name = 'tuesmon-contrib-letschat',
    version = ":versiontools:tuesmon_contrib_letschat:",
    description = "The Tuesmon plugin for LetsChat integration",
    long_description = "",
    keywords = 'tuesmon, letschat, integration',
    author = 'Andrea Stagi',
    author_email = 'stagi.andrea@gmail.com',
    url = 'https://github.com/tuesmoncom/tuesmon-contrib-letschat',
    license = 'AGPL',
    include_package_data = True,
    packages = find_packages(),
    install_requires=[],
    setup_requires = [
        'versiontools >= 1.9',
    ],
    classifiers = [
        "Programming Language :: Python",
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
