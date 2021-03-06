#!/usr/bin/env python
from setuptools import setup
import os

fp = open(os.path.join(os.path.dirname(__file__), "README.rst"))
readme_text = fp.read()
fp.close()

setup(
    name='CleverCSS',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    maintainer='David Ziegler',
    maintainer_email='david.ziegler@gmail.com',
    version='0.2',
    url='http://sandbox.pocoo.org/clevercss/',
    download_url='http://github.com/dziegler/clevercss/tree',
    packages=['clevercss'],
    scripts=['bin/ccss'],
    install_requires=['cssutils'],
    description='python inspired sass-like css preprocessor',
    long_description=readme_text,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
    test_suite = 'tests.all_tests',
)
