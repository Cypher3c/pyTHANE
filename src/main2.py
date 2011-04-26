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

foo.readXML("asset.xml")
foo.parseXML()

adham_asset =  foo.list["Adham"]

print adham_asset.commodities

foo.writeXML()

foo.saveXML("output.xml")
