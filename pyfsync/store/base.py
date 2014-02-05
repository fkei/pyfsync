#-*- coding: utf-8 -*-

import os
import logging

from pyfsync.hash import gen_hash, gen_file_hash

class BaseStore:
    pass
    def __init__(self):
        pass

    def walk(self, base_path):
        for root, dirs, files in os.walk(base_path):
            print "----------------"
            for f in files:
                key = "%s/%s" % (root, f)
                hash = gen_file_hash(key)
                self.propagation()
                self.manage["dbs"]["src"].put(key, hash)
                self.logger.debug("put: %s : %s" % (key, hash))
                #print self.manage["dbs"]["src"].get(key)

    def propagation(self):
        #import pdb; pdb.set_trace()
        for (k,v) in self.manage["peer"].items():
            if k is self.hash:
                continue

            #


            peer = self.manage["peer"][k]
            #self.logger.debug("target propagation:", peer.rootdir)
            #self.manage[k].sync()


    #
