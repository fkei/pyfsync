#-*- coding: utf-8 -*-

import os.path
import logging

import pyfsync

from pyfsync.store import FSStore, BaseStore

from pyfsync.db import setup_db

class FSync():
    """
    """

    #def __init__(self, *args, **kwargs):
    def __init__(self, options):
        """
        """
        self.logger = logging.getLogger('pyfsync')
        self.logger.info(options)

        #import pdb; pdb.set_trace()

        if not options["src"]["dir"]:
            raise pyfsync.PyFSyncError('source directory path is not set. path=%s' % options["src"]["dir"])

        if not options["dst"]["dir"]:
            raise pyfsync.PyFSyncError('destination directory path is not set. path=%s' % options["dst"]["dir"])

        if not os.path.isdir(options["src"]["dir"]):
            raise pyfsync.PyFSyncError('source directory is not a directory. path=%s' % options["src"]["dir"])

        if not os.path.isdir(options["dst"]["dir"]):
            raise pyfsync.PyFSyncError('destination directory is not a directory. path=%s' % options["dst"]["dir"])


        if isinstance(options["store"]["class"], object) is False:
            raise pyfsync.PyFSyncError('Definition misses the store class. %s' % str(options["store"]["class"]))

        if isinstance(options["store"]["db"], object) is False:
            raise pyfsync.PyFSyncError('Definition misses the db class. %s' % str(options["store"]["db"]))

        # manage

        self.manage = {
            "options": options,
            "peer": {},
            "seed": None,
            "dbs": None
        }

        # db
        self.manage["dbs"] = setup_db(options)

        # store
        options = self.manage["options"]

        # seed
        seed = options["store"]["class"](options["src"]["dir"], self.manage)
        self.manage["seed"] = seed
        self.manage["peer"][seed.hash] = seed

        # peer

        dst = options["store"]["class"](options["dst"]["dir"], self.manage)

        self.manage["peer"][dst.hash] = dst;


        # update
        self.manage["seed"].update()
