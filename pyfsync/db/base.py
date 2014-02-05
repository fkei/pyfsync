#-*- coding: utf-8 -*-

import pyfsync

class BaseDB:
    """
    """
    def __init__(self):
        self.db = None

    def get(self, key):
        raise pyfsync.PyFSyncError('DB get api not support.')

    def put(self, key, value):
        raise pyfsync.PyFSyncError('DB put api not support.')

    def delete(self, key):
        raise pyfsync.PyFSyncError('DB delete api not support.')
