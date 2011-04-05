'''
Created on Mar 28, 2011

@author: Cypher
'''
from lxml import etree
from lxml import objectify

class nxList: #List of Naev xml-derived objects (see below)
    alist = {} #dict of assets
    tree = None # XML tree
    root = None #root elem
    
    def readXML(self, _filename):
        #Load file
        fileobject = open(_filename, "r") #read-only
        self.tree = objectify.parse(fileobject)
        self.root = self.tree.getroot()

class nxObject: #Naev xml-derived object
    a_name = None
    node = None #the node in the tree that the object was derived from
    attrib = {} #values in a dict
    attribPaths = {} #corresponding Xpaths (Keys must be the same as in attribute!!!)
    
    flag = {} #boolean values in a dict
    flagPaths = {} #corresponding Xpaths (Keys must be the same as in flag!!!)
    
    list = {} #dict of param lists :P
    listPaths = {} #correspondign Xpaths (Keys must be the same as in flag!!!)
    
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
            
    def getlistX(self, root, x_path, _list, tag): 
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
    def setflagX(self, root, x_path, _flag): 
        ''' Writes flag to tree: deletes if false and already exists
        and adds if true but doesn't exist yet)
        '''
        try:
            if root.xpath(x_path):
                if not self.flag[_flag]: 
                    #delete value
                    temp1 = root.xpath(x_path)
                    temp1.getparent().remove(temp1)
                    #yeah, pretty ugly
        except AttributeError:
            #element does not exist, so create it if true value is here
            #first, see if parent tag of list items exists, create it if neccesary
            #split xpath into leader and item
            leader = x_path.rpartition("/")[0]
            item = x_path.rpartition("/")[2]
            
           # if :
           #     pass