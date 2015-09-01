# coding: utf-8

from __future__ import absolute_import

from .b import B


class A:
    def __init__(self):
        pass

    def test(self):
        return B().test()
