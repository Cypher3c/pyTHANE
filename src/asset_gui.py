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
    
    def __init__(self, parent=None):
       super(assetDialog, self).__init__(parent)
       self.setupUi(self)
       self.setWindowTitle("pyTHANE")
       
       ##Set connections
       
       #open file
       QtCore.QObject.connect(self.action_Open, QtCore.SIGNAL('triggered()'),
                              self.open_file) 
       #load asset info
       
       self.assetList.currentTextChanged.connect(self.getAsset)
       
       #delete asset
       self.deleteButton.clicked.connect(self.delAsset)
       
       ##
       
       #Define Asset List
       self.alist = schema.AssetList()
       
    def open_file(self):
        self.currOpenFile = QtGui.QFileDialog.getOpenFileName(self, "Open File", 
                                                         filter = "XML Files (*.xml)")
        self.alist.readXML(str(self.currOpenFile))
        self.alist.parseXML()
        
        self.setWindowTitle("pyTHANE - %s" % self.currOpenFile)
        self.populateAssetList()
        
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
    
    def setAsset(self):
        '''Changes the data for the currently selected asset
        '''
        
    
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
