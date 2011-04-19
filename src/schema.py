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
        for elem in self.root:
            temp_asset = Asset()
            a_name = elem.get("name")
            temp_asset.node = elem
            temp_asset.readALLattributes(elem)
            self.list[a_name] = temp_asset
    
    def writeXML(self):
        for ob_name, ob in self.list.iteritems():
            if ob.modified:
                ob.clear()
                ob.writeALLattributes(ob.node)
                
class CommodityList(base.nxList):
    pass
    



class Asset(base.nxObject):
    def __init__(self):
        #set variables 
        type = "asset"       
        self.attrib.append(["Is_virtual", False, 'virtual', 'flag'])
        self.attrib.append(["X_pos", None, 'pos/x', 'attrib'])
        self.attrib.append(["Y_pos", None, 'pos/y', 'attrib'])
        self.attrib.append(["Space_GFX", None, 'GFX/space', 'attrib'])
        self.attrib.append(["Ext_GFX", None, 'GFX/exterior', 'attrib'])
        self.attrib.append(["Faction", None, 'presence/faction', 'attrib'])
        self.attrib.append(["Faction_value", "0.000000", 'presence/value', 'attrib'])
        self.attrib.append(["Faction_range", "0", 'presence/range', 'attrib'])
        self.attrib.append(["Class", "A", 'general/class', 'attrib'])
        self.attrib.append(["Population", "0", 'general/population', 'attrib'])
        self.attrib.append(["Is_land", False, 'general/services/land', 'flag'])
        self.attrib.append(["Is_refuel", False, 'general/services/refuel', 'flag'])
        self.attrib.append(["Is_bar", False, 'general/services/bar', 'flag'])
        self.attrib.append(["Is_missions", False, 'general/services/missions', 'flag'])
        self.attrib.append(["Is_commodities", False, 'general/services/commodity', 'flag'])
        self.attrib.append(["Is_outfits", False, 'general/services/outfits', 'flag'])
        self.attrib.append(["Is_shipyard", False, 'general/services/shipyard', 'flag'])
        self.attrib.append(["Commodities", [], 'general/commodities/commodity', 'list'])
        self.attrib.append(["Description", "(null)", 'general/description', 'attrib'])
        self.attrib.append(["Bar_description", "(null)", 'general/bar', 'attrib'])
        self.attrib.append(["Tech", [], 'tech/item', 'list'])
                                            
class Commodity(base.nxObject):
    def __init__(self):
        pass