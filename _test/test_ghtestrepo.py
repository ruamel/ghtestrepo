# coding 'utf-8'

from __future__ import print_function

import pytest                         # NOQA

from ruamel.ghtestrepo import GH_TestRepo


# default for tox stub is to Fail
def test_ghtestrepo():
    t = GH_TestRepo()
    assert t.test()
