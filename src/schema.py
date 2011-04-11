'''
assets.py
Created on Jan 17, 2011

@author: Cypher
License: GPLv3
'''
import base
from lxml import etree
from lxml import objectify

class AssetList(base.nxList):
    
    
    def parseXML(self):
        '''Parses the xml tree loaded
        '''
        for elem in self.root.asset:
            temp_asset = Asset()
            a_name = elem.get("name") # get name, which is the key for dict
            temp_asset.node = elem
            temp_asset.getALLattributesX(elem)
            temp_asset.getALLflagsX(elem)
            temp_asset.getALLlistsX(elem)
            self.alist[a_name] = temp_asset

class CommodityList(base.nxList):
    
    def parseXML(self):
        '''Parses the xml tree loaded
        '''
        for elem in self.root.asset:
            temp_commodity = Commodity()
            a_name = elem.get("name") # get name, which is the key for dict
            temp_commodity.node = elem
            temp_commodity.getALLattributesX(elem)
            self.alist[a_name] = temp_commodity
            del temp_commodity
    


    
    

class Asset(base.nxObject):
    def __init__(self):
        #set variables
        self.attrib = {"X_pos" : None,  
                       "Y_pos" : None, 
                       "Space_GFX" : None, 
                       "Ext_GFX" : None,
                       "Faction" : None,
                       "Faction_value" : None,
                       "Faction_range" : None,
                       "Class" : None,
                       "Population" : None,
                       "Description" : None,
                       "Bar_Description" : None}
        self.attribPaths = {"X_pos" : 'pos/x',  
                            "Y_pos" : 'pos/y', 
                            "Space_GFX" : 'GFX/space', 
                            "Ext_GFX" : 'GFX/exterior',
                            "Faction" : 'presence/faction',
                            "Faction_value" : 'presence/value',
                            "Faction_range" : 'presence/range',
                            "Class" : 'general/class',
                            "Population" : 'general/population',
                            "Description" : 'general/description',
                            "Bar_Description" : 'general/bar'}
        #set flags
        self.flag = {"is_land" : False,
                     "is_refuel" : False,
                     "is_bar" : False,
                     "is_missions" : False,
                     "is_commodities" : False,
                     "is_outfits" : False,
                     "is_shipyard" : False}
        self.flagPaths = {"is_land" : 'general/services/land',
                     "is_refuel" : 'general/services/refuel',
                     "is_bar" : 'general/services/bar',
                     "is_missions" : 'general/services/missions',
                     "is_commodities" : 'general/services/commodity',
                     "is_outfits" : 'general/services/outfits',
                     "is_shipyard" : 'general/services/shipyard'}
        #set lists
        self.list = {"Commodities" : [],
                     "Tech" : []}
        self.listPaths = {"Commodities" : 'general/commodities/commodity',
                     "Tech" : 'tech/item'}
        
class Commodity(base.nxObject):
    def __init__(self):
        #set variables
        self.attrib = {"Description" : None,  
                       "Price" : None}
        