'''
Created on Mar 28, 2011

@author: Cypher
'''
from lxml import etree

class nxList: #List of Naev xml-derived objects (see below)
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
        
    def addobject(self, _name):
        
        pass
    
    def renameobject(self, _oldname, _newname):
        pass
    
    def copyobject(self, _origin, _target):
        pass
    
class nxObject: #Naev xml-derived object
    a_name = None
    node = None #the node in the tree that the object was derived from 
    attrib = []
    #       0                   1         2      3
    #[name of attribute, default value, xpath, type (attribute, flag, list)]
    
    misload = False
    
    modified = False
    
    def find_item(self, key):
        for index, sublist in enumerate(self.attrib):
            if sublist[0] == key:
                return index
    
    def clear(self):
        '''
        deletes all the child nodes of the object in quesion
        Permits it to be rewritten
        '''
        for elem in self.node.iterchildren():
            self.node.remove(elem)
    
    #List of functions to import values from xml trees 
    #and save them into the list
            
    def readattribute(self, _root, _index):
        '''
        read in attribute using root object and index of value in list
        ''' 
        if self.attrib[_index][3] == 'attrib':
            try:
                self.attrib[_index][1] = _root.xpath(self.attrib[_index][2]).text
            except KeyError:
                self.misload = True
            except AttributeError:
                pass 
        elif self.attrib[_index][3] == 'flag':
            try:
                if _root.xpath(self.attrib[_index][2]):
                    self.attrib[_index][1] = True
            except KeyError:
                self.misload = True
            except AttributeError:
                self.attrib[_index][1] = False 
        elif self.attrib[_index][3] == 'list':
            try:
                #get tag name
                tag_name = self.attrib[_index][4]
                _node = _root.xpath(self.attrib[_index][2])
                for item in _node:
                    self.attrib[_index][1].append(item.text)
            except KeyError:
                self.misload = True
            #except AttributeError:
               # print ("error in %s" % _index)
        
    def readALLattributes(self, _root):
        i = 0
        while i < len(self.attrib):
            self.readattribute(_root, i)
            i = i + 1
            
    
    #List of functions to save stuff back to xml trees
    def writetag(self, _root, x_path, text = False): 
        """
        _root: lxml.etree.Element, the object being described
        x_path: string like 'x/y/z', anything more complex is likely to break
        text: the text to write, ignore if false
        """        
        nodes = _root.xpath(x_path)
        parts = x_path.split('/')
        p = _root
        for part in parts: # make sure elements do not already exist
            nodes = p.xpath(part)
            if not nodes:
                n = etree.XML("<%s/>" % part)
                p.append(n)
                p = n
            else:
                p = nodes[0]
        node = p
        if text:
            node.text = str(text)
        
        return node
            
    def writeattribute(self, _root, _index): 
        
        if self.attrib[_index][3] == 'attrib':
            if self.attrib[_index][1]: #if attribute has a value, write it
                self.writetag(_root, self.attrib[_index][2], str(self.attrib[_index][1]))   
        
        elif self.attrib[_index][3] == 'flag':
            if self.attrib[_index][1]: #if attribute has a value, write it
                self.writetag(_root, self.attrib[_index][2])
                
        elif self.attrib[_index][3] == 'list':
            #f len(self.attrib[_index][1]) > 0:
                parent_x_path = self.attrib[_index][2].rpartition[/]
                #get tag name
                tag_name = self.attrib[_index][4]
                #make parent tag
                node = self.writetag(_root, parent_x_path)
            
                #now make each element
                _list = self.attrib[_index][1]
                for item in _list:
                    list_item = etree.SubElement(node, tag_name)
                    node.append(list_item)
                    list_item.text = item
                pass
    def writeALLattributes(self, _root): 
        i = 0 
        while i < len(self.attrib):
            self.writeattribute(_root, i) 
            i = i + 1