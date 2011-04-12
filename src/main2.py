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

foo.readXML("test.xml")
foo.parseXML()


#Change Missions to true

foo.list["Adham"].flag["is_missions"] = True
foo.list["Adham"].flag["is_refuel"] = False
foo.list["Adham"].modified = True
foo.list["Adham"].clear()
foo.writeALLXML()

foo.writeXML("output.xml")