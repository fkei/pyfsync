#-*- coding: utf-8 -*-

import os.path
import sys

import pytest

import pyfsync
from pyfsync.store import FSStore
from pyfsync.db import Level

def test_FSync():
    testsdir = os.path.abspath(os.path.dirname(__file__))
    src = "%s/fs/src" % testsdir
    dst = "%s/fs/dst" % testsdir

    #pytest.set_trace()

    #assert 1 == 0
    fsync = pyfsync.FSync({
        "store": {
            "db": Level,
            "class": FSStore,
            "context": {
                "dir": "%s/fs/store" % testsdir
            }
        },
        "src": {
            "dir": src
        },
        "dst": {
            "dir": dst
        }
    })



if __name__ == "__main__":
    pytest.main()
