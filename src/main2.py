'''
Created on Jan 17, 2011

@author: Cypher
License: GPLv3
'''

import schema
import pickle

print "pyTHANE v0.0.4, pythonized THANE"
print ""
print "by Cypher, licensed under GPLv3"

foo = schema.AssetList()

foo.readXML("test.xml")
foo.parseXML()

for k,v in sorted(foo.alist.iteritems()):
    print k
    print v.attrib
    print v.flag
    print v.list
       