# Copyright (c) 2016-2017, Adam Karpierz
# Licensed under the BSD license
# http://opensource.org/licenses/BSD-3-Clause

from __future__ import absolute_import

from os import path
from setuptools import setup
from codecs import open as fopen
fread = lambda name, encoding="utf-8": fopen(name, "r", encoding).read()

top_dir = path.dirname(path.abspath(__file__))

with open(path.join(top_dir, "pcap", "__about__.py")) as f:
    class about: exec(f.read(), None)

setup(
    name             = about.__title__,
    version          = about.__version__,
    description      = about.__summary__,
    url              = about.__uri__,
    download_url     = about.__uri__,

    author           = about.__author__,
    author_email     = about.__email__,
    maintainer       = about.__author__,
    maintainer_email = about.__email__,
    license          = about.__license__,
    long_description = (fread(path.join(top_dir, "README.rst")) + "\n" +
                        fread(path.join(top_dir, "CHANGES.rst"))),
)
