'''
Created on Mar 28, 2011

@author: Cypher
'''
from lxml import etree
from lxml import objectify

class nxList: #List of Naev xml-derived objects (see below)
    list = {} #dict of assets
    tree = None # XML tree
    root = None #root elem
    
    def readXML(self, _filename):
        #Load file
        fileobject = open(_filename, "r") #read-only
        self.tree = objectify.parse(fileobject)
        self.root = self.tree.getroot()
        
    def writeXML(self, _filename):
        fileobject = open(_filename,"w")
        self.tree.write(fileobject, pretty_print=True)
        
    def addobject(self, _name):
        pass
    
    def renameobject(self, _oldname, _newname):
        pass
    
    def copyobject(self, _origin, _target):
        pass

class nxObject: #Naev xml-derived object
    a_name = None
    node = None #the node in the tree that the object was derived from
    attrib = {} #values in a dict
    attribPaths = {} #corresponding Xpaths (Keys must be the same as in attribute!!!)
    
    flag = {} #boolean values in a dict
    flagPaths = {} #corresponding Xpaths (Keys must be the same as in flag!!!)
    
    list = {} #dict of param lists :P
    listPaths = {} #corresponding Xpaths (Keys must be the same as in flag!!!)
    
    misload = False
    
    #List of functions to import values from xml trees 
    #and save them into dicts
    
    def getattributeX(self, node, x_path, _attrib): 
        '''Gets a value from an xml node indicated by an xpath
        and assigns it to a the appropriate. If node does not exists
        it assigns "error"
        '''
        
        try:
            self.attrib[_attrib] = node.xpath(x_path)
        except KeyError:
            self.misload = True
        except AttributeError:
            pass

    def getflagX(self, root, x_path, _flag): 
        '''Sees if a tag exists. If it does, assigns true to flag,
        otherwise assigns false to flag
        '''
        try:
            if root.xpath(x_path):
                self.flag[_flag] = True
        except KeyError:
            self.misload = True
        except AttributeError:
            self.flag[_flag] = False
            
    def getlistX(self, root, x_path, _list): 
        '''Gets lists of params
        '''
        try:
            if root.xpath(x_path):
                temp_list_node = root.xpath(x_path)
                for item in temp_list_node:
                    self.list[_list].append(item)
        except KeyError:
            self.misload = True
        except AttributeError:
            pass
        
    def getALLattributesX(self, _root):
        '''Uses getattributeX and parses through the attribute dict, assigning
        values as it goes. _root is the main document root'''
        for k in self.attrib:
            self.getattributeX(_root, self.attribPaths[k], k)
            
    def getALLflagsX(self, _root):
        '''Uses getflagX and parses through the attribute dict, assigning
        true/false as it goes. _root is the main document root'''
        for k in self.flag:
            self.getflagX(_root, self.flagPaths[k], k)
    
    def getALLlistsX(self, _root):
        '''Uses getlistX and gets all the lists
        '''
        for k in self.list:
            self.getlistX(_root, self.listPaths[k], k)
            
            
    #List of functions to save stuff back to xml trees
    def writetag(self, _root, x_path, value, text = False): 
        """
        _root: lxml.etree.Element, the object being described
        x_path: string like 'x/y/z', anything more complex is likely to break
        value: false = delete node if exists, true = create if doesn't exist
        text: the text to write, ignore if false
        """        
        nodes = _root.xpath(x_path)
        if nodes:
            node = nodes[0]
        else: #try to create node
            #split path into elements
            parts = x_path.split('/')
            p = _root
            for part in parts:
                nodes = p.xpath(part)
                if not nodes:
                    n = etree.XML("<%s/>" % part)
                    p.append(n)
                    p = n
                else:
                    p = nodes[0]
            node = p
        if value is False:
            node.getparent().remove(node)
        else:
            if text:
                node.text = str(value)
    
    def writetaglist(self, _root, x_path, _list):       
        '''
        _list is the list to parse through
        '''
        parent_x_path = x_path.rpartition('/')[0]
        
        nodes = _root.xpath(parent_x_path)
        if nodes:
            node = nodes[0]
        else:
            parts = parent_x_path.split('/')
            p = _root
            for part in parts:
                nodes = p.xpath(part)
                if not nodes:
                    n = etree.XML("<%s/>" % part)
                    p.append(n)
                    p = n
                else:
                    p = nodes[0]
            node = p
    
    def writeattributeX(self, _root, x_path, _attrib): 
        ''' Writes attrib to tree with value in text
        '''
        if self.attrib[_attrib]: #if attribute has a value, write it
            self.writetag(_root, self.attribPaths[_attrib], True, self.attrib[_attrib])
        else: #otherwise, delete it
            self.writetag(_root, self.attribPaths[_attrib], False)
        
    def writeflagX(self, _root, x_path, _flag): 
        ''' Writes flag to tree: deletes if false and already exists
        and adds if true but doesn't exist yet)
        '''
        self.writetag(_root, self.flagPaths[_flag], self.flag[_flag])
    def writelistX(self, _root, x_path, _list): 
        ''' writes list to tree; somewhat different in that it writes from
        each item on the list in the dict, so it has its own writing routine
        '''
        pass #TODO
       
    def writeALLattributesX(self, _root):
        '''
        writes all attributes
        '''
        for k in self.attrib:
          self.writeattributeX(_root, self.attribPaths[k], k)  
    
    def writeALLflagsX(self, _root):
        '''
        writes all flags
        '''
        for k in self.flag:
          self.writeflagX(_root, self.flagPaths[k], k)  
    