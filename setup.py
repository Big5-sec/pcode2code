#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

#with open('HISTORY.rst') as history_file:
#    history = history_file.read()

requirements = ["pcodedmp"]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Nicolas Zilio",
    author_email='nicolas.zilio@hotmail.fr',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="a vba p-code decompiler based on pcodedmp",
    entry_points={
        'console_scripts': [
            'pcode2code=pcode2code.pcode2code:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n', # + history,
    long_description_content_type = 'text/markdown',
    include_package_data=True,
    keywords='pcode2code',
    name='pcode2code',
    packages=find_packages(include=['pcode2code', 'pcode2code.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Big5_sec/pcode2code',
    version='0.1.1',
    zip_safe=False,
)
