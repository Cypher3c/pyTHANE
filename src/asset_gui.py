'''
Created on May 1, 2011

@author: Cypher
'''

from PyQt4 import QtCore, QtGui
import asset_dialog
import schema
import sys

    
class assetDialog(QtGui.QMainWindow, asset_dialog.Ui_MainWindow):
    
    alist = None
    currOpenFile = None
    assetWidgets = []
    saved_path = None
    
    file_loaded = None #path to file loaded, or none if nothing loaded
    
    temp_asset = None #place to store current params
    temp_asset_name = None #place to store current asset name
    
    def __init__(self, parent=None):
       super(assetDialog, self).__init__(parent)
       self.setupUi(self)
       self.setWindowTitle("pyTHANE 0.5.0 ")
       
       
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
       
       #set virtual
       
       self.virtualCheck.toggled.connect(self.set_virtual)
       
       
       #changed fields (the save button's status serves as a modified flag)
    
       self.nameBox.textChanged.connect(self.set_modified)
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
    
    def set_virtual(self, _bool):
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
    def select_asset(self, _name):
        self.getAsset(_name)
        
    def new_asset(self):
        '''Make a new asset, prompting for name
        '''
        reply, ok = QtGui.QInputDialog.getText(self, 'New Asset', 'Please enter a name for the asset')
        
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
            
    def changeAssetName(self, _original, _new):
        self.alist.copy(_original, _new)
        #self.delAsset()
            
    def getAsset(self, _name):
        '''get the asset info into the form based on the selection from the list
        _name: the text of the asset clicked
        '''
        
        #change _name from Qstring to string
        
        name = str(_name)
        
        
        #Clear the form
        self.nameBox.clear()
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
        
        #set nameBox
        self.nameBox.setText(name)
        
        #set virtualCheck, and, if checked, ignore the rest
        if self.alist.list[name].virtual:
            self.virtualCheck.setChecked(True)
            self.set_virtual(True)
        else:
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
        
        #disable save button
        self.saveButton.setDisabled(True)
    def saveAsset(self):
        '''Changes the data for the asset
        _name: name of the asset to set data for
        '''
        #get name
        name = str(self.assetList.currentItem().text())
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
    
    def delAsset(self):
        ''' Deletes the currently selected asset from the asset list and the listbox
        '''
        
        
        name = str(self.assetList.currentItem().text())

        #remove listbox entry
        self.assetList.takeItem(self.assetList.currentRow())
        
        #delete from asset list
        del self.alist.list[name]
     
    def newAsset(self):
        '''Make a new asset
        '''
        pass #TODO   
        
app = QtGui.QApplication(sys.argv)
foo = assetDialog()
foo.show()
sys.exit(app.exec_())
