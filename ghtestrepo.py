# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import

import sys                # NOQA
import os                 # NOQA

from . import __version__

from .a import A


class GH_TestRepo(object):
    def __init__(self):
        self.version = __version__

    def test(self):
        x = A()
        return x.test()
