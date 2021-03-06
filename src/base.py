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
    
    #XML stuff
    def readXML(self, _filename):
        '''Loads an XML file into a tree object.
        _filename: the xml file to load
        '''
        #Load file
        fileobject = open(_filename, "r") #read-only
        parser = etree.XMLParser(remove_blank_text=True)
        self.tree = etree.parse(fileobject, parser)
        self.root = self.tree.getroot()
        
    def saveXML(self, _filename):
        '''Saves the XML tree back to a file
        _filename: the xml file to save to.
        '''
        fileobject = open(_filename,"w")
        fileobject.write(etree.tostring(self.tree, pretty_print=True))
        
    #Copy stuff
    def copy(self, _source, _destination):
        '''Copy an object in the list
        _source: the name of the object to copy from
        _destination the name of the copy to copy to
        '''
        self.list[_destination] = self.list[_source]
    
class nxObject: #Naev xml-derived object
    #name = None
    node = None #the node in the tree that the object was derived from

    misload = False
    
    modified = False 
