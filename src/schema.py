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
                del temp_asset
    
    def writeXML(self):
        for nam, ob in self.list.iteritems():
            a_node = ob
            a_node.write()
class CommodityList(base.nxList):
    pass
    



class Asset(base.nxObject):
    """An Asset (planet/station)"""
    
    #Variables
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
    
    
    description = "(null)"
    bar_description = "(null)"
    
    commodities = []
    tech = []
    
    def __init__(self):
        self.commodities = []
        self.tech = []
    
    #Parsing stuff
    
    def parse(self, _node, _name):
        """Parse xml node and assign values to variables
        _node: the node of the base object (i.e. <asset>)
        _name: the name of the asset that is being parsed
        
        """
        self.name = _name
        self.node = _node
        
        stop_comm_check = False #to stop parsing commodities, needed to fix issues
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
            elif elem.tag == "general":
                for ge_elem in elem:
                    if ge_elem.tag == "class":
                        self.asset_class = ge_elem.text                        
                    elif ge_elem.tag == "population":
                        self.population = ge_elem.text
                    elif ge_elem.tag == "services":
                        for s_elem in ge_elem:
                            if s_elem.tag == "land":
                                self.is_land = True
                            elif s_elem.tag == "refuel":
                                self.is_refuel = True
                            elif s_elem.tag == "bar":
                                self.is_bar = True
                            elif s_elem.tag == "missions":
                                self.is_missions = True
                            elif s_elem.tag == "commodity":
                                self.is_commodity = True
                            elif s_elem.tag == "outfits":
                                self.is_outfits = True
                            elif s_elem.tag == "shipyard":
                                self.is_shipyard = True
                    elif ge_elem.tag == "commodities":
                        if len(ge_elem):
                            for c_elem in ge_elem:
                                if c_elem.tag == "commodity":
                                    self.commodities.append(c_elem.text)
                    elif ge_elem.tag == "description":
                        self.description = ge_elem.text
                    elif ge_elem.tag == "bar":
                        self.bar_description = ge_elem.text
            elif elem.tag == "tech":
                for t_elem in elem:
                    if t_elem.tag == "item":
                        self.tech.append(t_elem.text)
                        
    def write(self):
        """Writes the asset back to the tree (overwrites existing)
        _node: the node (<asset>) to write to
        
        """
        #first, clear existing contents
        self.node.clear() #note: this also deletes name attribute, so...
        self.node.set("name", self.name) #re-write name, handy if changed
        #start building asset
        if self.virtual: #if virtual, just write virtual tag and presence info
            virt_tag = etree.SubElement(self.node, "virtual")
            presence_tag = etree.SubElement(self.node, "presence")
            fac_tag = etree.SubElement(presence_tag, "faction")
            fac_tag.text = self.faction
            val_tag = etree.SubElement(presence_tag, "value")
            val_tag.text = self.value_faction
            rang_tag = etree.SubElement(presence_tag, "range")
            rang_tag = self.range_faction
            
        else:
            if self.x_pos or self.y_pos:
                pos_tag = etree.SubElement(self.node, "pos")
                x_tag = etree.SubElement(pos_tag, "x")
                x_tag.text = self.x_pos
                y_tag = etree.SubElement(pos_tag, "y")
                y_tag.text = self.y_pos
             
            if self.space_gfx or self.exterior_gfx:
                gfx_tag = etree.SubElement(self.node, "GFX")
                s_gfx_tag = etree.SubElement(gfx_tag, "space")
                s_gfx_tag.text = self.space_gfx
                e_gfx_tag = etree.SubElement(gfx_tag, "exterior")
                e_gfx_tag.text = self.exterior_gfx
            pres_tag = etree.SubElement(self.node, "presence")
            
            if self.faction:
                fac_tag = etree.SubElement(pres_tag, "faction")
                fac_tag.text = self.faction
            val_tag = etree.SubElement(pres_tag, "value")
            rang_tag = etree.SubElement(pres_tag, "range")
            if self.value_faction:
                val_tag.text = self.value_faction
            else:
                val_tag.text = "0.000000"
            rang_tag.text = self.range_faction
            
            gen_tag = etree.SubElement(self.node, "general")  
            class_tag = etree.SubElement(gen_tag, "class")
            class_tag.text = self.asset_class
            pop_tag = etree.SubElement(gen_tag, "population")   
            pop_tag.text = self.population
            
            serv_tag = etree.SubElement(gen_tag, "services")
            if self.is_land:
                land_tag = etree.SubElement(serv_tag, "land")
            if self.is_refuel:
                refuel_tag = etree.SubElement(serv_tag, "refuel")
            if self.is_bar:
                bar_tag = etree.SubElement(serv_tag, "bar")
            if self.is_missions:
                missions_tag = etree.SubElement(serv_tag, "missions")
            if self.is_commodity:
                commodity_tag = etree.SubElement(serv_tag, "commodity")   
            if self.is_outfits:
                outfits_tag = etree.SubElement(serv_tag, "outfits") 
            if self.is_shipyard:
                shipyard_tag = etree.SubElement(serv_tag, "shipyard")
            
            comm_list_tag = etree.SubElement(gen_tag, "commodities")
            if len(self.commodities) > 0: # check and see if any commodities exist
                for comm in self.commodities:
                    temp_item = etree.Element("commodity")
                    temp_item.text = comm
                    comm_list_tag.append(temp_item)
                    del temp_item
            
            descrip_tag = etree.SubElement(gen_tag, "description")
            descrip_tag.text = self.description
            bar_descrip_tag = etree.SubElement(gen_tag, "bar")
            bar_descrip_tag.text = self.bar_description
            
            if len(self.tech) > 0:
                tech_tag = etree.SubElement(self.node, "tech")
                for item in self.tech:
                    temp_thing = etree.Element("item")
                    temp_thing.text = item
                    tech_tag.append(temp_thing)
                    del temp_thing
class Commodity(base.nxObject):
    def __init__(self):
        pass