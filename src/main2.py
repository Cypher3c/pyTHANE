'''
Created on Jan 17, 2011

@author: Cypher
License: GPLv3
'''

import schema
import pickle

print "pyTHANE v0.1.0, pythonized THANE"
print ""
print "by Cypher, licensed under GPLv3"

foo = schema.AssetList()

foo.readXML("test4.xml")
foo.parseXML()


#Change Missions to true

foo.alist["Adham"].flag["is_missions"] = True
foo.alist["Adham"].flag["is_refuel"] = False
foo.alist["Adham"].writeALLflagsX(foo.alist["Adham"].node)

foo.writeXML("output.xml")