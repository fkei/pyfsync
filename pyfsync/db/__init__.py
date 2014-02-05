#-*- coding: utf-8 -*-

import os

from pyfsync.db.base import *
from pyfsync.db.level import *

def setup_db(options):
    store = options["store"]
    basedir = store["context"]["dir"]

    bin_path = "%s/bin.db" % (options["store"]["context"]["dir"])
    op_path = "%s/op.db" % (options["store"]["context"]["dir"])
    src_path = "%s/src.db" % (options["store"]["context"]["dir"])
    dst_path = "%s/dst.db" % (options["store"]["context"]["dir"])

    # create base dir
    if os.path.isdir(bin_path) is False:
        os.makedirs(bin_path)
    if os.path.isdir(op_path) is False:
        os.makedirs(op_path)
    if os.path.isdir(src_path) is False:
        os.makedirs(src_path)
    if os.path.isdir(dst_path) is False:
        os.makedirs(dst_path)

    return {
        "bin": store["db"](bin_path), # Binary log
        "op": store["db"](op_path), # operation log
        "src": store["db"](src_path), # hash src fs
        "dst": store["db"](dst_path) # hash src fs
    }
