'''
assets.py
Created on Jan 17, 2011

@author: Cypher
License: GPLv3
'''
import obs
from lxml import etree
from lxml import objectify

class Asset(obs.nxObject):
    ###List of params
    aname = None
    
    isvirtual = False
    #Location params
    posX = None #1 --error flag for missing part
    posY = None #2
    #GFX params
    spaceGFX = None #4
    extGFX = None #8
    #Presence params
    faction = None #None means no faction #16
    facvalue = None #32
    facrange = None #64
    #Planet/Station params
    assetclass = None #128
    population = None #256
    #Service params, defined as false by default
    island = False  #512
    isrefuel = False
    isbar = False
    ismissions = False
    iscommodity = False
    isoutfits = False
    isshipyard = False
    #Descriptions
    description = "(null)"
    bardescription = "(null)"
    
    commodities = []
    
    ##Functions
    
    def __init__(self,nam="unknown"):
        self.aname = nam
    
        
        #Functions to set variables; defaults (i.e. arguments not given) are ignored
        #called like this: Foo.set(x position, y position)
        #Virtual can't be set this way, because it has a different set of variables
        #Also, tech lists cannot be set this way due to it being stored in a list TODO
        
        #The only catch is that you can't assign a variable the value of "default_arg",
        #so don't give that name to any planets :P
        
        #Typecheck flag tells function to look for attribute errors (use only if parsing XML) ----TODO
    def set_pos(self, x_pos = "default_arg", y_pos  = "default_arg"):
        if not self.isvirtual: #don't write values to virtual asset
            if x_pos != "default_arg":
                self.posX = x_pos
            if y_pos != "default_arg":
                self.posY = y_pos
            
    def set_gfx(self, space = "default_arg", exterior  = "default_arg"):
        if not self.isvirtual:
            if space != "default_arg":
                self.spaceGFX = space
            if exterior != "default_arg":
                self.extGFX = exterior
                
    def set_presence(self, faction = "default_arg", value  = "default_arg", range  = "default_arg"):
        if faction != "default_arg":
            self.faction = faction
        if value != "default_arg":
            self.facvalue = value
        if range != "default_arg":
            self.facrange = range
                                
        #Setting an asset as virt is handled in its own method.
    def set_virtual(self, is_virtual):
        #Check and see if system is already virtual
        if(self.isvirtual == True):
            if is_virtual == False: #if input is false
                self.isvirtual = False
        else: #system is not virtual
            if is_virtual == True: #but input is
                self.isvirtual = True
                #Delete unused variables
                #self.posX = self.posY = self.spaceGFX = self.extGFX = self.assetclass = self.population = None
                #self.island = self.isrefuel = self.isbar = self.ismissions = self.iscommodity = self.isoutfits = self.isshipyard = False
                #self.description = self.bardescription = None
    def set_services(self, land = "default_arg", refuel = "default_arg", bar = "default_arg", missions = "default_arg", commodity = "default arg",
    outfits = "default_arg", shipyard = "default arg"):              
        pass
    def purge(self):  #deletes all vars
            ###List of params
        aname = None
        
        isvirtual = False
        #Location params
        posX = None
        posY = None
        #GFX params
        spaceGFX = None
        extGFX = None
        #Presence params
        faction = None #None means no faction
        facvalue = None
        facrange = None
        #Planet/Station params
        assetclass = None
        population = None
        #Service params, defined as false by default
        island = False
        isrefuel = False
        isbar = False
        ismissions = False
        iscommodity = False
        isoutfits = False
        isshipyard = False
        #Descriptions
        description = None
        bardescription = None
    
class AssetList:
    
    alist = [] #list of assets
    tree = None # XML tree
    root = None #root elem
    
    def loadXML(self,filenam):
        #Load file
        fileobject = open(filenam, "r") #read-only
        self.tree = objectify.parse(fileobject)
        self.root = self.tree.getroot()
        i = 0 #iterative var
        for elem in self.root.asset:
            temp_asset = Asset()# temp asset
            try: #catch missing name attribute
                temp_asset.aname = elem.get("name")
            except AttributeError:
                pass
            
            #Is Asset Virtual?
            virt = False
            try:
                if elem.virtual.tag:
                    virt = True
                    temp_asset.set_virtual(True)
            except AttributeError:
                temp_asset.set_virtual(False)
            if virt: #if virtual, get only faction, value, and range for presence
                try:
                    fac = elem.presence.faction
                except AttributeError:
                    fac = "faction tag not found"
                    temp_asset.misload = True
                try:
                    val = elem.presence.value
                except AttributeError:
                    val = "value tag not found"
                    temp_asset.misload = True
                try:
                    rang = elem.presence.range
                except AttributeError:
                    rang = "range tag not found"
                    temp_asset.misload = True
                #Set presence values
                temp_asset.set_presence(fac, val, rang)
            else: #if not virtual
                try:
                    temp_asset.set_pos(elem.pos.x, elem.pos.y)
                    temp_asset.set_gfx(elem.GFX.space, elem.GFX.exterior)
                except AttributeError:
                    temp_asset.misload = True
                try:
                    if elem.presence.faction:
                        temp_asset.set_presence(faction = elem.presence.faction, value = elem.presence.value, range = elem.presence.range)
                except AttributeError:
                        temp_asset.set_presence(value = 0, range = 0)
            self.alist.append(temp_asset) #add asset 
            temp_asset.purge()
            
    def sloadXML(self,filenam):
        #Load file
        fileobject = open(filenam, "r") #read-only
        self.tree = objectify.parse(fileobject)
        self.root = self.tree.getroot()
        i = 0 #iterative var
        for elem in self.root.asset:
            temp_asset = Asset()# temp asset
            try: #catch missing name attribute
                temp_asset.aname = elem.get("name")
            except AttributeError:
                temp_asset.aname = "boo"
            self.alist.append(temp_asset)
            del(temp_asset)
            i = i + 1

class tAssetList:
    
    alist = {} #dict of assets
    tlist = []
    tree = None # XML tree
    root = None #root elem
    
    def readXML(self, _filename):
        #Load file
        fileobject = open(_filename, "r") #read-only
        self.tree = objectify.parse(fileobject)
        self.root = self.tree.getroot()
        
        for elem in self.root.asset:
            temp_asset = tAsset()
            a_name = elem.get("name") # get name, which is the key for dict
            temp_asset.getALLattributesX(elem)
            self.alist[a_name] = temp_asset
            self.tlist.append(a_name)
    

class tAsset(obs.nxObject):
    def __init__(self):
        self.attrib = {"X_pos" : None,  "Y_pos" : None}
        self.attribPaths = {"X_pos" : 'pos/x',  "Y_pos" : 'pos/y'}
        