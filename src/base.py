'''
Created on Mar 28, 2011

@author: Cypher
'''
from lxml import etree

class nxList: #List of Naev xml-derived objects
    list = {} #dict of assets
    tree = None # XML tree
    root = None #root elem
    type = None
    
    
    def readXML(self, _filename):
        #Load file
        fileobject = open(_filename, "r") #read-only
        parser = etree.XMLParser(remove_blank_text=True)
        self.tree = etree.parse(fileobject, parser)
        self.root = self.tree.getroot()
        
    def saveXML(self, _filename):
        fileobject = open(_filename,"w")
        fileobject.write(etree.tostring(self.tree, pretty_print=True))
    
class nxObject: #Naev xml-derived object
    name = None
    node = None #the node in the tree that the object was derived from 

    misload = False
    
    modified = False    