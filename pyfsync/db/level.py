#-*- coding: utf-8 -*-

from leveldb import LevelDB
from pyfsync.db.base import BaseDB

class Level():

    def __init__(self, db_path):
        self.db_path = db_path
        self.db = LevelDB(self.db_path)

    def get(self, key):
        return self.db.Get(key)

    def put(self, key, value):
        return self.db.Put(key, value)

    def delete(self, key):
        return self.db.Delete


    #def create_snapshot(self):
    #def get_stats(self):
    #def range_iter(self):
    #def write(self):
