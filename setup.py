#!/usr/bin/env python
import re
from setuptools import setup

_version_re = re.compile(r"__version__\s=\s'(.*)'")


with open('loginpass/__init__.py', 'r') as f:
    version = _version_re.search(f.read()).group(1)


with open('README.rst') as read_me:
    long_description = read_me.read()


setup(
    name='loginpass',
    version=version,
    description='Social connections powered by Authlib for Flask and Django',
    long_description=long_description,
    url='https://authlib.org/',
    zip_safe=False,
    license='AGPLv3+',
    packages=['loginpass'],
    install_requires=['Authlib'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)