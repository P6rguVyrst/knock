#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
===============================
HtmlTestRunner
===============================


.. image:: https://img.shields.io/pypi/v/knock.svg
        :target: https://pypi.python.org/pypi/knock
.. image:: https://img.shields.io/travis/P6rguvyrst/knock.svg
        :target: https://travis-ci.org/P6rguvyrst/knock

Knock on ports on different IP addresses to see if they're open.


Links:
---------
* `Github <https://github.com/P6rguvyrst/knock>`_
"""

from setuptools import setup, find_packages

requirements = [ ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Toomas Ormisson",
    author_email='toomas.ormisson@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Knock on ports on different IP addresses to see if they're open.",
    install_requires=requirements,
    license="MIT license",
    long_description=__doc__,
    include_package_data=True,
    keywords='knock',
    name='knock',
    packages=find_packages(include=['knock']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/P6rguvyrst/knock',
    version='0.1.0',
    zip_safe=False,
)
