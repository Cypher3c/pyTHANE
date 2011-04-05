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
            node = elem
            temp_asset.getALLattributesX(elem)
            temp_asset.getALLflagsX(elem)
            temp_asset.getALLlistsX(elem)
            self.alist[a_name] = temp_asset
            del temp_asset

class CommodityList(base.nxList):
    
    def parseXML(self):
        '''Parses the xml tree loaded
        '''
        for elem in self.root.asset:
            temp_commodity = Commodity()
            a_name = elem.get("name") # get name, which is the key for dict
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
        self.flag = {"Is_land" : False,
                     "Is_refuel" : False,
                     "Is_bar" : False,
                     "Is_missions" : False,
                     "Is_commodity" : False,
                     "Is_outfits" : False,
                     "Is_shipyard" : False}
        self.flagPaths = {"Is_land" : 'general/services/land',
                     "Is_refuel" : 'general/services/refuel',
                     "Is_bar" : 'general/services/bar',
                     "Is_missions" : 'general/services/missions',
                     "Is_commodity" : 'general/services/commodity',
                     "Is_outfits" : 'general/services/outfits',
                     "Is_shipyard" : 'general/services/shipyard'}
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
        