'''
Created on Jan 17, 2011

@author: Cypher
License: GPLv3
'''

import schema
from lxml import etree

print "pyTHANE v0.2.0, pythonized THANE"
print ""
print "by Cypher, licensed under GPLv3"

foo = schema.AssetList()

foo.readXML("test.xml")
foo.parseXML()

print foo.list["Adham"].space_gfx

print foo.list["Adham"].x_pos