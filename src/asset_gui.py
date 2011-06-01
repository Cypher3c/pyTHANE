'''
Created on May 1, 2011

@author: Cypher
'''

from PyQt4 import QtCore, QtGui
import asset_dialog
import schema
import sys
import os
import ConfigParser

    
class assetDialog(QtGui.QMainWindow, asset_dialog.Ui_MainWindow):
    
    alist = None
    currOpenFile = None
    assetWidgets = []
    saved_path = None
    Naev_dir = None
    conf_file = None
    conf_parser = None
    
    space_gfx_list = []
    exterior_gfx_list = []
    space_gfx_pic = None
    exterior_gfx_pic = None
    default_gfx_pic = None
    
    file_loaded = None #path to file loaded, or none if nothing loaded
    
    temp_asset = None #place to store current params
    temp_asset_name = None #place to store current asset name
    
    def __init__(self, parent=None):
        super(assetDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("pyTHANE 0.1.2 ")
       
       
        #Define Asset List
        self.alist = schema.AssetList()
       
        #Define temp Asset
        self.temp_asset = schema.Asset()
       
        ##Set connections
       
        #open file
        QtCore.QObject.connect(self.action_Open, QtCore.SIGNAL('triggered()'),
                              self.open_file) 
       
        #save file
        self.action_Save.triggered.connect(self.save_file)
       
        #save as file
        self.action_Save_as.triggered.connect(self.save_as_file)
       
        #load asset info
       
        self.assetList.currentTextChanged.connect(self.getAsset)
       
        #save asset
        self.saveButton.clicked.connect(self.saveAsset)
       
        #delete asset
        self.deleteButton.clicked.connect(self.delAsset)
       
        #New asset
        self.newButton.clicked.connect(self.new_asset)
       
        #Rename Asset
        self.renameButton.clicked.connect(self.rename_Asset)
       
        #Copy Asset
        self.copyButton.clicked.connect(self.copyAsset)
       
        #set virtual
        self.virtualCheck.toggled.connect(self.set_virtual)
        
        #set Naev dir
        self.actionSet_Naev_Directory.triggered.connect(self.set_Naev_dir)
        
        #Space/exterior Graphics
        self.spaceRadio.toggled.connect(self.load_GFX)
       
        #changed fields (the save button's status serves as a modified flag)
        self.populationBox.textChanged.connect(self.set_modified)
        self.classBox.textChanged.connect(self.set_modified)
        self.descriptionBox.textChanged.connect(self.set_modified)
        self.bardescriptionBox.textChanged.connect(self.set_modified)
        self.virtualCheck.stateChanged.connect(self.set_modified)
        self.landCheck.stateChanged.connect(self.set_modified)
        self.barCheck.stateChanged.connect(self.set_modified)
        self.refuelCheck.stateChanged.connect(self.set_modified)
        self.missionCheck.stateChanged.connect(self.set_modified)
        self.outfitCheck.stateChanged.connect(self.set_modified)
        self.commodityCheck.stateChanged.connect(self.set_modified)
        self.shipyardCheck.stateChanged.connect(self.set_modified)
       
        ##
       
        #Import naev dir location from conf file, if possible
        #Load conf file
        self.conf_file = open("asset.conf", "r")
        self.conf_parser = ConfigParser.RawConfigParser()
        self.conf_parser.readfp(self.conf_file)
        if self.conf_parser.has_section("Options"):
            if self.conf_parser.has_option("Options", "Naev_Directory"):
                self.Naev_dir = self.conf_parser.get("Options", "Naev_Directory")
                #Check if path exists
                if not os.path.exists((self.Naev_dir + "/gfx")):
                    self.Naev_dir = None
        
        #set the space and exterior graphics lists
        self.get_spaceGFX()
        self.get_exteriorGFX()
    
        self.load_GFX(True)
        
        self.space_gfx_pic = QtGui.QPixmap()
        self.exterior_gfx_pic = QtGui.QPixmap()
        self.default_gfx_pic = QtGui.QPixmap()
        self.default_gfx_pic.load("noimage.png")
        self.gfxLabel.setPixmap(self.default_gfx_pic)
        
    def set_virtual(self, _bool):
            self.populationBox.setDisabled(_bool)
            self.classBox.setDisabled(_bool)
            self.descriptionBox.setDisabled(_bool)
            self.bardescriptionBox.setDisabled(_bool)
            self.landCheck.setDisabled(_bool)
            self.barCheck.setDisabled(_bool)
            self.refuelCheck.setDisabled(_bool)
            self.missionCheck.setDisabled(_bool)
            self.outfitCheck.setDisabled(_bool)
            self.commodityCheck.setDisabled(_bool)
            self.shipyardCheck.setDisabled(_bool)
    def set_modified(self):
        
        if not self.saveButton.isEnabled():
            self.saveButton.setEnabled(True)
            
    def clear(self):
        '''Clear the form
        '''
        self.populationBox.clear()
        self.classBox.clear()
        self.descriptionBox.clear()
        self.bardescriptionBox.clear()
        
        
        self.virtualCheck.setChecked(False)
        
        self.landCheck.setChecked(False)
        self.barCheck.setChecked(False)
        self.refuelCheck.setChecked(False)
        self.missionCheck.setChecked(False)
        self.outfitCheck.setChecked(False)
        self.commodityCheck.setChecked(False)
        self.shipyardCheck.setChecked(False)
        
    def select_asset(self, _name):
        self.getAsset(_name)
        
    def new_asset(self):
        '''Make a new asset, prompting for name
        '''
        i = True
        while i:
            reply, ok = QtGui.QInputDialog.getText(self, 'New Asset', 'Please enter a name for the asset')
            try:
                check = self.assetList.findItems(reply, QtCore.Qt.MatchCaseSensitive)[0]
            except IndexError:
                i = False
        
        if ok and reply:
            #add new asset to dict
            self.alist.new(str(reply))
            #and to list
            self.assetList.addItem(reply)
            #sort list
            self.assetList.sortItems(QtCore.Qt.AscendingOrder)
            #get item
            _item = self.assetList.findItems(reply, QtCore.Qt.MatchCaseSensitive)[0]
            #scroll to item
            self.assetList.scrollToItem(_item, QtGui.QAbstractItemView.PositionAtCenter)
            #select item
            self.assetList.setItemSelected(_item, True)
            #clear form
            self.clear()
            #load its params
            self.getAsset(reply)
            
    def open_file(self):
        self.currOpenFile = QtGui.QFileDialog.getOpenFileName(self, "Open File", 
                                                         filter = "XML Files (*.xml)")
        if self.currOpenFile:
            self.alist.readXML(str(self.currOpenFile))
            self.alist.parseXML()
        
            self.setWindowTitle("pyTHANE - %s" % self.currOpenFile)
            self.populateAssetList()
    def save_file(self):
        #if file does not exist yet, prompt for name and path
        if not self.currOpenFile:
            self.currOpenFile = QtGui.QFileDialog.getSaveFileName(parent=self, caption="Save XML file", filter="XML Files (*.xml)")
        
        if self.currOpenFile:
            #write xml tree
            self.alist.writeXML()
            
            #now save file
            self.alist.saveXML(str(self.currOpenFile))
            
    def save_as_file(self):
        self.currOpenFile = QtGui.QFileDialog.getSaveFileName(parent=self, caption="Save XML file", filter="XML Files (*.xml)")
        #write xml tree
        
        if self.currOpenFile:
            self.alist.writeXML()
            
            #now save file
            self.alist.saveXML(str(self.currOpenFile)) 
        
    def populateAssetList(self):
        #clear asset box
        self.assetList.clear()
        for name in sorted(self.alist.list.keys()):
            self.assetList.addItem(name)
            
    def getAsset(self, _name):
        '''get the asset info into the form based on the selection from the list
        _name: the text of the asset clicked
        '''
        
        #change _name from Qstring to string
        
        name = str(_name)
        
        #clear form
        self.clear()
        
        #set virtualCheck, and, if checked, ignore the rest
        if self.alist.list[name].virtual:
            self.virtualCheck.setChecked(True)
            self.set_virtual(True)
            self.setImage(name)
        else:
            self.populationBox.setText(self.alist.list[name].population)
            self.classBox.setText(self.alist.list[name].asset_class)
            if not self.alist.list[name].description == "(null)":
                self.descriptionBox.setPlainText(self.alist.list[name].description)
            if not self.alist.list[name].bar_description == "(null)":
                self.bardescriptionBox.setPlainText(self.alist.list[name].bar_description)
            
            self.landCheck.setChecked(self.alist.list[name].is_land)
            self.refuelCheck.setChecked(self.alist.list[name].is_refuel)
            self.barCheck.setChecked(self.alist.list[name].is_bar)
            self.missionCheck.setChecked(self.alist.list[name].is_missions)
            self.commodityCheck.setChecked(self.alist.list[name].is_commodity)
            self.outfitCheck.setChecked(self.alist.list[name].is_outfits)
            self.shipyardCheck.setChecked(self.alist.list[name].is_shipyard)
            self.setImage(name)
        #disable save button
        self.saveButton.setDisabled(True)
    
    def setGFXCombo(self, name):
        #return index
        if self.spaceRadio.isChecked:
            if self.alist.list[name].space_gfx:
                self.gfxCombo.setCurrentIndex(self.gfxCombo.findText(self.alist.list[name].space_gfx))
            else:
                self.gfxCombo.setCurrentIndex("0")
        else:
            if self.alist.list[name].exterior_gfx:
                self.gfxCombo.setCurrentIndex(self.gfxCombo.findText(self.alist.list[name].exterior_gfx))
            else:
                self.gfxCombo.setCurrentIndex("0")
        #return
    def setImage(self, name):
        if self.Naev_dir:
            #set graphics
            
            if self.spaceRadio.isChecked:
                if self.alist.list[name].space_gfx:
                    self.space_gfx_pic.load((self.Naev_dir + "/gfx/planet/space/" + self.alist.list[name].space_gfx))
                else:
                    self.space_gfx_pic.load("noimage.png")
            else:
                if self.alist.list[name].exterior_gfx:
                    self.space_gfx_pic.load((self.Naev_dir + "/gfx/planet/exterior/" + self.alist.list[name].exterior_gfx))
                else:
                    self.space_gfx_pic.load("noimage.png")
            self.gfxLabel.setPixmap(self.space_gfx_pic.scaled(220, 220))
            self.setGFXCombo(name)
    def saveAsset(self):
        '''Changes the data for the asset
        '''
        name = str(self.assetList.currentItem().text())
        self.alist.list[name].population = str(self.populationBox.text())
        self.alist.list[name].asset_class = str(self.classBox.text())
        if str(self.descriptionBox.toPlainText()):
            self.alist.list[name].description = str(self.descriptionBox.toPlainText())
        else:
            self.alist.list[name].description = "(null)"
        if str(self.bardescriptionBox.toPlainText()):
            self.alist.list[name].bar_description = str(self.bardescriptionBox.toPlainText())
        else:
            self.alist.list[name].bar_description = "(null)"
        self.alist.list[name].virtual = self.virtualCheck.isChecked()
        self.alist.list[name].is_land = self.landCheck.isChecked()
        self.alist.list[name].is_refuel = self.refuelCheck.isChecked()
        self.alist.list[name].is_bar = self.barCheck.isChecked()
        self.saveButton.setDisabled(True)
        
    def rename_Asset(self):
        '''Changes the name of the asset
        '''
        i = True
        while i:
            reply, ok = QtGui.QInputDialog.getText(self, 'Rename Asset', 'Please enter a name for the asset')
            try:
                check = self.assetList.findItems(reply, QtCore.Qt.MatchCaseSensitive)[0]
            except IndexError:
                i = False
            if not ok:
                i = False
        if ok and reply:
            #copy asset
            self.alist.copy(str(self.assetList.currentItem().text()), str(reply))
            #Delete old asset
            del self.alist.list[str(self.assetList.currentItem().text())]
            
            #Add to list
            self.assetList.addItem(reply)
            #Remove old item
            self.assetList.takeItem(self.assetList.currentRow())
            #sort list
            self.assetList.sortItems(QtCore.Qt.AscendingOrder)
            #get item
            _item = self.assetList.findItems(reply, QtCore.Qt.MatchCaseSensitive)[0]
            #scroll to item
            self.assetList.scrollToItem(_item, QtGui.QAbstractItemView.PositionAtCenter)
            #select item
            self.assetList.setItemSelected(_item, True)
            #clear form
            self.clear()
            #load its params
            self.getAsset(reply)
    
    def delAsset(self):
        ''' Deletes the currently selected asset from the asset list and the listbox
        '''
        name = str(self.assetList.currentItem().text())

        #remove listbox entry
        self.assetList.takeItem(self.assetList.currentRow())
        
        #delete from asset list
        del self.alist.list[name]
        
    def copyAsset(self):
        i = True
        while i:
            reply, ok = QtGui.QInputDialog.getText(self, 'Copy Asset', 'Please enter a name for the new asset')
            try:
                check = self.assetList.findItems(reply, QtCore.Qt.MatchCaseSensitive)[0]
            except IndexError:
                i = False
            if not ok:
                i = False
        if ok and reply:
            #copy asset
            self.alist.copy(str(self.assetList.currentItem().text()), str(reply))
            #Add to list
            self.assetList.addItem(reply)
            #sort list
            self.assetList.sortItems(QtCore.Qt.AscendingOrder)
            #get item
            _item = self.assetList.findItems(reply, QtCore.Qt.MatchCaseSensitive)[0]
            #scroll to item
            self.assetList.scrollToItem(_item, QtGui.QAbstractItemView.PositionAtCenter)
            #select item
            self.assetList.setItemSelected(_item, True)
            #clear form
            self.clear()
            #load its params
            self.getAsset(reply)
        
    def set_Naev_dir(self):
        if self.Naev_dir:
            reply = QtGui.QFileDialog.getExistingDirectory(parent=self, caption="Select Naev Directory", directory = self.Naev_dir)
        else:
            reply = QtGui.QFileDialog.getExistingDirectory(parent=self, caption="Select Naev Directory")
        if reply:
            self.Naev_dir = str(reply)
            #write to config file
            self.conf_file = open("asset.conf", "r+")
            self.conf_parser.readfp(self.conf_file)
            self.conf_parser.set("Options", "Naev_Directory", self.Naev_dir)
            self.conf_parser.write(self.conf_file)
    def alert_noNaevDir(self):
            QtGui.QMessageBox.warning(self, "Naev Directory Not Set", "You must set the Naev directory \n before you can set that parameter.")
    
    def get_spaceGFX(self):
        if self.Naev_dir:
            #clear the list of space GFX
            del self.space_gfx_list[:]
            space_gfx_dir = self.Naev_dir + "/gfx/planet/space/"
            spaceList = os.listdir(space_gfx_dir)
            for fname in spaceList:
                self.space_gfx_list.append(fname)
    def get_exteriorGFX(self):
        if self.Naev_dir:
        #clear the list of exterior graphics
            del self.exterior_gfx_list[:]
            exterior_gfx_dir = self.Naev_dir + "/gfx/planet/exterior/"
            extList = os.listdir(exterior_gfx_dir)
            for fname in extList:
                self.exterior_gfx_list.append(fname)
            
    def load_GFX(self, _bool):
        '''Load the appropriate graphics into the combo box
        _bool: checked/unchecked status of space radiobox
        '''
        #first, clear box
        self.gfxCombo.clear()
        #if Naev directory set:
        if self.Naev_dir:
            if _bool:
            #populate gfx combo box with spaceGFX
                self.gfxCombo.addItem("Select Item")
                for _item in sorted(self.space_gfx_list):
                    self.gfxCombo.addItem(_item)
            else:
                self.gfxCombo.addItem("Select Item")
                for _item in sorted(self.exterior_gfx_list):
                    self.gfxCombo.addItem(_item)
        else:
            self.gfxCombo.addItem("Set Naev Dir First")
            
    #def 
app = QtGui.QApplication(sys.argv)
asset_instance = assetDialog()
asset_instance.show()
sys.exit(app.exec_())
