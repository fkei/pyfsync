#-*- coding: utf-8 -*-

import logging

from pyfsync.hash import gen_hash
from pyfsync.store.base import BaseStore

class FSStore(BaseStore):
    """
    """
    def __init__(self, rootdir, manage):
        self.logger = logging.getLogger('pyfsync.store.fs')

        self.hash = gen_hash(rootdir)
        self.rootdir = rootdir
        self.manage = manage

    def update(self):
        self.walk(self.rootdir)
