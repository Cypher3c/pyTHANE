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
        #set the textboxes
        self.nameBox.setText(_name)
        self.descriptionBox.setText(self.alist.list[str(_name)].description)
    
app = QtGui.QApplication(sys.argv)
foo = assetDialog()
foo.show()
sys.exit(app.exec_())
