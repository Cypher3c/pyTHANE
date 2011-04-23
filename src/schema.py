'''
assets.py
Created on Jan 17, 2011

@author: Cypher
License: GPLv3
'''
import base
from lxml import etree

class AssetList(base.nxList):
    
    def parseXML(self):
        """Parses each asset (must be called after readXML)"""
        
        for asset_elem in self.root:
            if asset_elem.tag == "asset":
                temp_asset = Asset()
                _name = asset_elem.get("name")
                temp_asset.parse(asset_elem, _name)
                self.list[_name] = temp_asset
    
    def writeXML(self):
        pass
    
class CommodityList(base.nxList):
    pass
    



class Asset(base.nxObject):
    """An Asset (planet/station)"""
    
    #Variables
    name = None
    
    virtual = False
    
    #Position
    x_pos = None
    y_pos = None
    
    #GFX
    space_gfx = None
    exterior_gfx = None
    
    #Presence
    faction = None
    value_faction = 0
    range_faction = 0
    
    #General
    asset_class = "A"
    population = 0
    
    #Services
    is_land = False
    is_refuel = False
    is_bar = False
    is_missions = False
    is_commodity = False
    is_outfits = False
    is_shipyard = False
    
    commodities = []
    
    description = "(null)"
    bar_description = "(null)"
    
    tech = []
    
    #Parsing stuff
    
    def parse(self, _node, _name):
        """Parse xml node and assign values to variables
        _node: the node of the base object (i.e. <asset>)
        _name: the name of the asset that is being parsed
        
        """
        self.name = _name
        for elem in _node:
            if elem.tag == "virtual":
                self.virtual = True
                continue
            elif elem.tag == "GFX":
                for g_elem in elem:
                    if g_elem.tag == "space":
                        self.space_gfx = g_elem.text
                    elif g_elem.tag == "exterior":
                        self.exterior_gfx = g_elem.text
            elif elem.tag == "pos":
                for p_elem in elem:
                    if p_elem.tag == "x":
                        self.x_pos = p_elem.text
                    if p_elem.tag == "y":
                        self.y_pos = p_elem.text
            elif elem.tag == "presence":
                for pr_elem in elem:
                    if pr_elem.tag == "faction":
                        self.faction = pr_elem.text
                    elif pr_elem.tag == "value":
                        self.value_faction = pr_elem.text
                    elif pr_elem.tag == "range":
                        self.range_faction = pr_elem.text
                                            
class Commodity(base.nxObject):
    def __init__(self):
        pass