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
       
       #Set connections
       QtCore.QObject.connect(self.action_Open, QtCore.SIGNAL('triggered()'),
                              self.open_file) 
       self.assetList.currentTextChanged.connect(self.getAsset)
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
            self.landCheck.setChecked(self.alist.list[name].is_land)
            self.refuelCheck.setChecked(self.alist.list[name].is_refuel)
            self.barCheck.setChecked(self.alist.list[name].is_bar)
            self.missionCheck.setChecked(self.alist.list[name].is_missions)
            self.commodityCheck.setChecked(self.alist.list[name].is_commodity)
            self.outfitCheck.setChecked(self.alist.list[name].is_outfits)
            self.shipyardCheck.setChecked(self.alist.list[name].is_shipyard)
app = QtGui.QApplication(sys.argv)
foo = assetDialog()
foo.show()
sys.exit(app.exec_())
