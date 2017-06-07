#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='qiscus_sdk',
    version='0.0.1',
    description="Python version of Qiscus SDK wrapper",
    long_description=readme + '\n\n' + history,
    author="Muhamad Ishlah",
    author_email='nurul.ishlah@gmail.com',
    url='https://github.com/nurulishlah/qiscus_sdk',
    packages=[
        'qiscus_sdk',
    ],
    package_dir={'qiscus_sdk':
                 'qiscus_sdk'},
    entry_points={
        'console_scripts': [
            'qiscus_sdk=qiscus_sdk.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='qiscus_sdk',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
