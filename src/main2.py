'''
Created on Jan 17, 2011

@author: Cypher
License: GPLv3
'''

import asset
import pickle

print "pyTHANE v0.0.4, pythonized THANE"
print ""
print "by Cypher, licensed under GPLv3"

foo = asset.tAssetList()

foo.readXML("test.xml")

for k,v in sorted(foo.alist.iteritems()):
    print k
    print v.attrib
    print v.flag
    print v.list
       