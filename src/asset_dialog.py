# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asset.ui'
#
# Created: Wed May  4 14:25:40 2011
#      by: PyQt4 UI code generator 4.7.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(861, 610)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 261, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.assetList = QtGui.QListWidget(self.verticalLayoutWidget)
        self.assetList.setObjectName("assetList")
        self.verticalLayout.addWidget(self.assetList)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(300, 50, 151, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.nameBox = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.nameBox.setObjectName("nameBox")
        self.horizontalLayout_3.addWidget(self.nameBox)
        self.horizontalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(450, 50, 91, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.virtualCheck = QtGui.QCheckBox(self.horizontalLayoutWidget_4)
        self.virtualCheck.setMouseTracking(False)
        self.virtualCheck.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.virtualCheck.setObjectName("virtualCheck")
        self.horizontalLayout_5.addWidget(self.virtualCheck)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(300, 90, 231, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.descriptionBox = QtGui.QLineEdit(self.horizontalLayoutWidget_3)
        self.descriptionBox.setObjectName("descriptionBox")
        self.horizontalLayout_8.addWidget(self.descriptionBox)
        self.serviceGroup = QtGui.QGroupBox(self.centralwidget)
        self.serviceGroup.setGeometry(QtCore.QRect(300, 220, 241, 171))
        self.serviceGroup.setAlignment(QtCore.Qt.AlignCenter)
        self.serviceGroup.setObjectName("serviceGroup")
        self.gridLayoutWidget = QtGui.QWidget(self.serviceGroup)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 221, 131))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.landCheck = QtGui.QCheckBox(self.gridLayoutWidget)
        self.landCheck.setObjectName("landCheck")
        self.gridLayout.addWidget(self.landCheck, 0, 0, 1, 1)
        self.refuelCheck = QtGui.QCheckBox(self.gridLayoutWidget)
        self.refuelCheck.setObjectName("refuelCheck")
        self.gridLayout.addWidget(self.refuelCheck, 0, 1, 1, 1)
        self.barCheck = QtGui.QCheckBox(self.gridLayoutWidget)
        self.barCheck.setObjectName("barCheck")
        self.gridLayout.addWidget(self.barCheck, 1, 0, 1, 1)
        self.commodityCheck = QtGui.QCheckBox(self.gridLayoutWidget)
        self.commodityCheck.setObjectName("commodityCheck")
        self.gridLayout.addWidget(self.commodityCheck, 1, 1, 1, 1)
        self.missionCheck = QtGui.QCheckBox(self.gridLayoutWidget)
        self.missionCheck.setObjectName("missionCheck")
        self.gridLayout.addWidget(self.missionCheck, 2, 0, 1, 1)
        self.outfitCheck = QtGui.QCheckBox(self.gridLayoutWidget)
        self.outfitCheck.setObjectName("outfitCheck")
        self.gridLayout.addWidget(self.outfitCheck, 2, 1, 1, 1)
        self.shipyardCheck = QtGui.QCheckBox(self.gridLayoutWidget)
        self.shipyardCheck.setObjectName("shipyardCheck")
        self.gridLayout.addWidget(self.shipyardCheck, 3, 0, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(570, 50, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 861, 25))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Options = QtGui.QMenu(self.menubar)
        self.menu_Options.setObjectName("menu_Options")
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_New = QtGui.QAction(MainWindow)
        self.action_New.setEnabled(False)
        self.action_New.setObjectName("action_New")
        self.action_Quit = QtGui.QAction(MainWindow)
        self.action_Quit.setObjectName("action_Quit")
        self.action_Open = QtGui.QAction(MainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Close = QtGui.QAction(MainWindow)
        self.action_Close.setEnabled(False)
        self.action_Close.setObjectName("action_Close")
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Close)
        self.menu_File.addAction(self.action_Quit)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Options.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.virtualCheck, QtCore.SIGNAL("clicked(bool)"), self.serviceGroup.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Assets", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.virtualCheck.setText(QtGui.QApplication.translate("MainWindow", "Virtual", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.serviceGroup.setTitle(QtGui.QApplication.translate("MainWindow", "Services", None, QtGui.QApplication.UnicodeUTF8))
        self.landCheck.setText(QtGui.QApplication.translate("MainWindow", "Land", None, QtGui.QApplication.UnicodeUTF8))
        self.refuelCheck.setText(QtGui.QApplication.translate("MainWindow", "Refuel", None, QtGui.QApplication.UnicodeUTF8))
        self.barCheck.setText(QtGui.QApplication.translate("MainWindow", "Bar", None, QtGui.QApplication.UnicodeUTF8))
        self.commodityCheck.setText(QtGui.QApplication.translate("MainWindow", "Commodities", None, QtGui.QApplication.UnicodeUTF8))
        self.missionCheck.setText(QtGui.QApplication.translate("MainWindow", "Missions", None, QtGui.QApplication.UnicodeUTF8))
        self.outfitCheck.setText(QtGui.QApplication.translate("MainWindow", "Outfits", None, QtGui.QApplication.UnicodeUTF8))
        self.shipyardCheck.setText(QtGui.QApplication.translate("MainWindow", "Shipyard", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Options.setTitle(QtGui.QApplication.translate("MainWindow", "&Options", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.action_New.setText(QtGui.QApplication.translate("MainWindow", "&New", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Quit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setText(QtGui.QApplication.translate("MainWindow", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setToolTip(QtGui.QApplication.translate("MainWindow", "Open an XML file", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Open.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Close.setText(QtGui.QApplication.translate("MainWindow", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))

