'''
Created on Jan 17, 2011

@author: Cypher
License: GPLv3
'''

import schema
from lxml import etree
import pickle

print "pyTHANE v0.1.0, pythonized THANE"
print ""
print "by Cypher, licensed under GPLv3"

foo = schema.AssetList()

foo.readXML("test.xml")
foo.parseXML()


#Change Missions to true for Adham
foo.list["Anecu"].attrib[foo.list["Anecu"].find_item("Is_missions")][1] = True
foo.list["Anecu"].attrib[foo.list["Anecu"].find_item("Is_refuel")][1] = False
foo.list["Anecu"].modified = True
foo.writeXML()

print foo.list["Anecu"].attrib[foo.list["Anecu"].find_item("Commodities")]

foo.saveXML("output.xml")