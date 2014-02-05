#-*- coding: utf-8 -*-

import os
import hashlib

def gen_file_hash(path):
    #s = str(os.stat(path).st_ctime) + os.stat(path).st_size + path
    s = str(os.stat(path).st_ctime) + path
    hex = hashlib.sha512(s).hexdigest()
    #print "sha512:", s, hex
    return hex

def gen_hash(s):
    hex = hashlib.sha512(s).hexdigest()
    return hex
