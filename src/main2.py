'''
Created on Jan 17, 2011

@author: Cypher
License: GPLv3
'''

import schema
from lxml import etree

print "pyTHANE v0.5.0, pythonized THANE"
print "Alpha 2"
print ""
print "by Cypher, licensed under GPLv3"

foo = schema.AssetList()

foo.readXML("asset.xml")
foo.parseXML()

adham_asset = foo.list["Ammu"]

print adham_asset.commodities

print adham_asset.tech

foo.writeXML()

foo.saveXML("output.xml")