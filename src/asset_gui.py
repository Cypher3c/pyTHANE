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
       QtCore.QObject.connect(self.action_Open, QtCore.SIGNAL('triggered()'),
                             self.open_file)
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
            print name
            self.assetList.addItem(name)
    
app = QtGui.QApplication(sys.argv)
foo = assetDialog()
foo.show()
sys.exit(app.exec_())
