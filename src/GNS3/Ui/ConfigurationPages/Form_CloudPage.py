# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ConfigurationPages/Form_CloudPage.ui'
#
# Created: Mon Sep  9 21:29:22 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CloudPage(object):
    def setupUi(self, CloudPage):
        CloudPage.setObjectName(_fromUtf8("CloudPage"))
        CloudPage.resize(542, 500)
        CloudPage.setWindowTitle(QtGui.QApplication.translate("CloudPage", "Cloud", None, QtGui.QApplication.UnicodeUTF8))
        self.vboxlayout = QtGui.QVBoxLayout(CloudPage)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.tabWidget = QtGui.QTabWidget(CloudPage)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.vboxlayout1 = QtGui.QVBoxLayout(self.tab)
        self.vboxlayout1.setObjectName(_fromUtf8("vboxlayout1"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setTitle(QtGui.QApplication.translate("CloudPage", "Generic Ethernet NIO (Administrator or root access required)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridlayout = QtGui.QGridLayout(self.groupBox)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.comboBoxGenEth = QtGui.QComboBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxGenEth.sizePolicy().hasHeightForWidth())
        self.comboBoxGenEth.setSizePolicy(sizePolicy)
        self.comboBoxGenEth.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.comboBoxGenEth.setObjectName(_fromUtf8("comboBoxGenEth"))
        self.gridlayout.addWidget(self.comboBoxGenEth, 0, 0, 1, 3)
        self.lineEditGenEth = QtGui.QLineEdit(self.groupBox)
        self.lineEditGenEth.setObjectName(_fromUtf8("lineEditGenEth"))
        self.gridlayout.addWidget(self.lineEditGenEth, 1, 0, 1, 1)
        self.pushButtonAddGenericEth = QtGui.QPushButton(self.groupBox)
        self.pushButtonAddGenericEth.setText(QtGui.QApplication.translate("CloudPage", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddGenericEth.setObjectName(_fromUtf8("pushButtonAddGenericEth"))
        self.gridlayout.addWidget(self.pushButtonAddGenericEth, 1, 1, 1, 1)
        self.pushButtonDeleteGenericEth = QtGui.QPushButton(self.groupBox)
        self.pushButtonDeleteGenericEth.setEnabled(False)
        self.pushButtonDeleteGenericEth.setText(QtGui.QApplication.translate("CloudPage", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDeleteGenericEth.setObjectName(_fromUtf8("pushButtonDeleteGenericEth"))
        self.gridlayout.addWidget(self.pushButtonDeleteGenericEth, 1, 2, 1, 1)
        self.listWidgetGenericEth = QtGui.QListWidget(self.groupBox)
        self.listWidgetGenericEth.setObjectName(_fromUtf8("listWidgetGenericEth"))
        self.gridlayout.addWidget(self.listWidgetGenericEth, 2, 0, 1, 3)
        self.vboxlayout1.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("CloudPage", "Linux Ethernet NIO (Linux only, root access required)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridlayout1 = QtGui.QGridLayout(self.groupBox_2)
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.comboBoxLinuxEth = QtGui.QComboBox(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxLinuxEth.sizePolicy().hasHeightForWidth())
        self.comboBoxLinuxEth.setSizePolicy(sizePolicy)
        self.comboBoxLinuxEth.setObjectName(_fromUtf8("comboBoxLinuxEth"))
        self.gridlayout1.addWidget(self.comboBoxLinuxEth, 0, 0, 1, 3)
        self.lineEditLinuxEth = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditLinuxEth.setObjectName(_fromUtf8("lineEditLinuxEth"))
        self.gridlayout1.addWidget(self.lineEditLinuxEth, 1, 0, 1, 1)
        self.pushButtonAddLinuxEth = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonAddLinuxEth.setText(QtGui.QApplication.translate("CloudPage", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddLinuxEth.setObjectName(_fromUtf8("pushButtonAddLinuxEth"))
        self.gridlayout1.addWidget(self.pushButtonAddLinuxEth, 1, 1, 1, 1)
        self.pushButtonDeleteLinuxEth = QtGui.QPushButton(self.groupBox_2)
        self.pushButtonDeleteLinuxEth.setEnabled(False)
        self.pushButtonDeleteLinuxEth.setText(QtGui.QApplication.translate("CloudPage", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDeleteLinuxEth.setObjectName(_fromUtf8("pushButtonDeleteLinuxEth"))
        self.gridlayout1.addWidget(self.pushButtonDeleteLinuxEth, 1, 2, 1, 1)
        self.listWidgetLinuxEth = QtGui.QListWidget(self.groupBox_2)
        self.listWidgetLinuxEth.setObjectName(_fromUtf8("listWidgetLinuxEth"))
        self.gridlayout1.addWidget(self.listWidgetLinuxEth, 2, 0, 1, 3)
        self.vboxlayout1.addWidget(self.groupBox_2)
        spacerItem = QtGui.QSpacerItem(21, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.vboxlayout1.addItem(spacerItem)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridlayout2 = QtGui.QGridLayout(self.tab_2)
        self.gridlayout2.setObjectName(_fromUtf8("gridlayout2"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setTitle(QtGui.QApplication.translate("CloudPage", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridlayout3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridlayout3.setObjectName(_fromUtf8("gridlayout3"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setText(QtGui.QApplication.translate("CloudPage", "Local port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout3.addWidget(self.label, 0, 0, 1, 1)
        self.spinBoxLocalPort = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxLocalPort.sizePolicy().hasHeightForWidth())
        self.spinBoxLocalPort.setSizePolicy(sizePolicy)
        self.spinBoxLocalPort.setMaximum(65535)
        self.spinBoxLocalPort.setProperty("value", 30000)
        self.spinBoxLocalPort.setObjectName(_fromUtf8("spinBoxLocalPort"))
        self.gridlayout3.addWidget(self.spinBoxLocalPort, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setText(QtGui.QApplication.translate("CloudPage", "Remote host:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout3.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEditRemoteHost = QtGui.QLineEdit(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditRemoteHost.sizePolicy().hasHeightForWidth())
        self.lineEditRemoteHost.setSizePolicy(sizePolicy)
        self.lineEditRemoteHost.setMinimumSize(QtCore.QSize(80, 0))
        self.lineEditRemoteHost.setText(QtGui.QApplication.translate("CloudPage", "127.0.0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditRemoteHost.setObjectName(_fromUtf8("lineEditRemoteHost"))
        self.gridlayout3.addWidget(self.lineEditRemoteHost, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setText(QtGui.QApplication.translate("CloudPage", "Remote port:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridlayout3.addWidget(self.label_3, 2, 0, 1, 1)
        self.spinBoxRemotePort = QtGui.QSpinBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxRemotePort.sizePolicy().hasHeightForWidth())
        self.spinBoxRemotePort.setSizePolicy(sizePolicy)
        self.spinBoxRemotePort.setMaximum(65535)
        self.spinBoxRemotePort.setProperty("value", 20000)
        self.spinBoxRemotePort.setObjectName(_fromUtf8("spinBoxRemotePort"))
        self.gridlayout3.addWidget(self.spinBoxRemotePort, 2, 1, 1, 1)
        self.gridlayout2.addWidget(self.groupBox_3, 0, 0, 1, 2)
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setTitle(QtGui.QApplication.translate("CloudPage", "NIOs", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.vboxlayout2 = QtGui.QVBoxLayout(self.groupBox_4)
        self.vboxlayout2.setObjectName(_fromUtf8("vboxlayout2"))
        self.listWidgetUDP = QtGui.QListWidget(self.groupBox_4)
        self.listWidgetUDP.setObjectName(_fromUtf8("listWidgetUDP"))
        self.vboxlayout2.addWidget(self.listWidgetUDP)
        self.gridlayout2.addWidget(self.groupBox_4, 0, 2, 2, 1)
        self.pushButtonAddUDP = QtGui.QPushButton(self.tab_2)
        self.pushButtonAddUDP.setText(QtGui.QApplication.translate("CloudPage", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddUDP.setObjectName(_fromUtf8("pushButtonAddUDP"))
        self.gridlayout2.addWidget(self.pushButtonAddUDP, 1, 0, 1, 1)
        self.pushButtonDeleteUDP = QtGui.QPushButton(self.tab_2)
        self.pushButtonDeleteUDP.setEnabled(False)
        self.pushButtonDeleteUDP.setText(QtGui.QApplication.translate("CloudPage", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDeleteUDP.setObjectName(_fromUtf8("pushButtonDeleteUDP"))
        self.gridlayout2.addWidget(self.pushButtonDeleteUDP, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 211, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout2.addItem(spacerItem1, 2, 1, 1, 1)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.vboxlayout3 = QtGui.QVBoxLayout(self.tab_3)
        self.vboxlayout3.setObjectName(_fromUtf8("vboxlayout3"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_5.setTitle(QtGui.QApplication.translate("CloudPage", "TAP interface (require root access)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridlayout4 = QtGui.QGridLayout(self.groupBox_5)
        self.gridlayout4.setObjectName(_fromUtf8("gridlayout4"))
        self.lineEditTAP = QtGui.QLineEdit(self.groupBox_5)
        self.lineEditTAP.setObjectName(_fromUtf8("lineEditTAP"))
        self.gridlayout4.addWidget(self.lineEditTAP, 0, 0, 1, 1)
        self.pushButtonAddTAP = QtGui.QPushButton(self.groupBox_5)
        self.pushButtonAddTAP.setText(QtGui.QApplication.translate("CloudPage", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddTAP.setObjectName(_fromUtf8("pushButtonAddTAP"))
        self.gridlayout4.addWidget(self.pushButtonAddTAP, 0, 1, 1, 1)
        self.pushButtonDeleteTAP = QtGui.QPushButton(self.groupBox_5)
        self.pushButtonDeleteTAP.setEnabled(False)
        self.pushButtonDeleteTAP.setText(QtGui.QApplication.translate("CloudPage", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDeleteTAP.setObjectName(_fromUtf8("pushButtonDeleteTAP"))
        self.gridlayout4.addWidget(self.pushButtonDeleteTAP, 0, 2, 1, 1)
        self.listWidgetTAP = QtGui.QListWidget(self.groupBox_5)
        self.listWidgetTAP.setObjectName(_fromUtf8("listWidgetTAP"))
        self.gridlayout4.addWidget(self.listWidgetTAP, 1, 0, 1, 3)
        self.vboxlayout3.addWidget(self.groupBox_5)
        spacerItem2 = QtGui.QSpacerItem(20, 191, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridlayout5 = QtGui.QGridLayout(self.tab_4)
        self.gridlayout5.setObjectName(_fromUtf8("gridlayout5"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_7.setTitle(QtGui.QApplication.translate("CloudPage", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.gridlayout6 = QtGui.QGridLayout(self.groupBox_7)
        self.gridlayout6.setObjectName(_fromUtf8("gridlayout6"))
        self.gridlayout7 = QtGui.QGridLayout()
        self.gridlayout7.setObjectName(_fromUtf8("gridlayout7"))
        self.label_5 = QtGui.QLabel(self.groupBox_7)
        self.label_5.setText(QtGui.QApplication.translate("CloudPage", "Local file:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridlayout7.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEditUNIXLocalFile = QtGui.QLineEdit(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditUNIXLocalFile.sizePolicy().hasHeightForWidth())
        self.lineEditUNIXLocalFile.setSizePolicy(sizePolicy)
        self.lineEditUNIXLocalFile.setObjectName(_fromUtf8("lineEditUNIXLocalFile"))
        self.gridlayout7.addWidget(self.lineEditUNIXLocalFile, 1, 0, 1, 1)
        self.gridlayout6.addLayout(self.gridlayout7, 0, 0, 1, 1)
        self.gridlayout8 = QtGui.QGridLayout()
        self.gridlayout8.setObjectName(_fromUtf8("gridlayout8"))
        self.label_6 = QtGui.QLabel(self.groupBox_7)
        self.label_6.setText(QtGui.QApplication.translate("CloudPage", "Remote file:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridlayout8.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEditUNIXRemoteFile = QtGui.QLineEdit(self.groupBox_7)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditUNIXRemoteFile.sizePolicy().hasHeightForWidth())
        self.lineEditUNIXRemoteFile.setSizePolicy(sizePolicy)
        self.lineEditUNIXRemoteFile.setObjectName(_fromUtf8("lineEditUNIXRemoteFile"))
        self.gridlayout8.addWidget(self.lineEditUNIXRemoteFile, 1, 0, 1, 1)
        self.gridlayout6.addLayout(self.gridlayout8, 1, 0, 1, 1)
        self.gridlayout5.addWidget(self.groupBox_7, 0, 0, 1, 2)
        self.groupBox_6 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_6.setTitle(QtGui.QApplication.translate("CloudPage", "NIOs", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.vboxlayout4 = QtGui.QVBoxLayout(self.groupBox_6)
        self.vboxlayout4.setObjectName(_fromUtf8("vboxlayout4"))
        self.listWidgetUNIX = QtGui.QListWidget(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetUNIX.sizePolicy().hasHeightForWidth())
        self.listWidgetUNIX.setSizePolicy(sizePolicy)
        self.listWidgetUNIX.setObjectName(_fromUtf8("listWidgetUNIX"))
        self.vboxlayout4.addWidget(self.listWidgetUNIX)
        self.gridlayout5.addWidget(self.groupBox_6, 0, 2, 3, 1)
        self.pushButtonAddUNIX = QtGui.QPushButton(self.tab_4)
        self.pushButtonAddUNIX.setText(QtGui.QApplication.translate("CloudPage", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddUNIX.setObjectName(_fromUtf8("pushButtonAddUNIX"))
        self.gridlayout5.addWidget(self.pushButtonAddUNIX, 1, 0, 1, 1)
        self.pushButtonDeleteUNIX = QtGui.QPushButton(self.tab_4)
        self.pushButtonDeleteUNIX.setEnabled(False)
        self.pushButtonDeleteUNIX.setText(QtGui.QApplication.translate("CloudPage", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDeleteUNIX.setObjectName(_fromUtf8("pushButtonDeleteUNIX"))
        self.gridlayout5.addWidget(self.pushButtonDeleteUNIX, 1, 1, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(160, 190, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridlayout5.addItem(spacerItem3, 2, 0, 2, 2)
        spacerItem4 = QtGui.QSpacerItem(196, 132, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout5.addItem(spacerItem4, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.gridlayout9 = QtGui.QGridLayout(self.tab_5)
        self.gridlayout9.setObjectName(_fromUtf8("gridlayout9"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_5)
        self.groupBox_8.setTitle(QtGui.QApplication.translate("CloudPage", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.gridlayout10 = QtGui.QGridLayout(self.groupBox_8)
        self.gridlayout10.setObjectName(_fromUtf8("gridlayout10"))
        self.gridlayout11 = QtGui.QGridLayout()
        self.gridlayout11.setObjectName(_fromUtf8("gridlayout11"))
        self.label_7 = QtGui.QLabel(self.groupBox_8)
        self.label_7.setText(QtGui.QApplication.translate("CloudPage", "Control file:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridlayout11.addWidget(self.label_7, 0, 0, 1, 1)
        self.lineEditVDEControlFile = QtGui.QLineEdit(self.groupBox_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditVDEControlFile.sizePolicy().hasHeightForWidth())
        self.lineEditVDEControlFile.setSizePolicy(sizePolicy)
        self.lineEditVDEControlFile.setObjectName(_fromUtf8("lineEditVDEControlFile"))
        self.gridlayout11.addWidget(self.lineEditVDEControlFile, 1, 0, 1, 1)
        self.gridlayout10.addLayout(self.gridlayout11, 0, 0, 1, 1)
        self.gridlayout12 = QtGui.QGridLayout()
        self.gridlayout12.setObjectName(_fromUtf8("gridlayout12"))
        self.label_8 = QtGui.QLabel(self.groupBox_8)
        self.label_8.setText(QtGui.QApplication.translate("CloudPage", "Local file:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridlayout12.addWidget(self.label_8, 0, 0, 1, 1)
        self.lineEditVDELocalFile = QtGui.QLineEdit(self.groupBox_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditVDELocalFile.sizePolicy().hasHeightForWidth())
        self.lineEditVDELocalFile.setSizePolicy(sizePolicy)
        self.lineEditVDELocalFile.setObjectName(_fromUtf8("lineEditVDELocalFile"))
        self.gridlayout12.addWidget(self.lineEditVDELocalFile, 1, 0, 1, 1)
        self.gridlayout10.addLayout(self.gridlayout12, 1, 0, 1, 1)
        self.gridlayout9.addWidget(self.groupBox_8, 0, 0, 1, 2)
        self.groupBox_9 = QtGui.QGroupBox(self.tab_5)
        self.groupBox_9.setTitle(QtGui.QApplication.translate("CloudPage", "NIOs", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.vboxlayout5 = QtGui.QVBoxLayout(self.groupBox_9)
        self.vboxlayout5.setObjectName(_fromUtf8("vboxlayout5"))
        self.listWidgetVDE = QtGui.QListWidget(self.groupBox_9)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetVDE.sizePolicy().hasHeightForWidth())
        self.listWidgetVDE.setSizePolicy(sizePolicy)
        self.listWidgetVDE.setObjectName(_fromUtf8("listWidgetVDE"))
        self.vboxlayout5.addWidget(self.listWidgetVDE)
        self.gridlayout9.addWidget(self.groupBox_9, 0, 2, 3, 1)
        self.pushButtonAddVDE = QtGui.QPushButton(self.tab_5)
        self.pushButtonAddVDE.setText(QtGui.QApplication.translate("CloudPage", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddVDE.setObjectName(_fromUtf8("pushButtonAddVDE"))
        self.gridlayout9.addWidget(self.pushButtonAddVDE, 1, 0, 1, 1)
        self.pushButtonDeleteVDE = QtGui.QPushButton(self.tab_5)
        self.pushButtonDeleteVDE.setEnabled(False)
        self.pushButtonDeleteVDE.setText(QtGui.QApplication.translate("CloudPage", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDeleteVDE.setObjectName(_fromUtf8("pushButtonDeleteVDE"))
        self.gridlayout9.addWidget(self.pushButtonDeleteVDE, 1, 1, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(161, 201, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.gridlayout9.addItem(spacerItem5, 2, 0, 2, 2)
        spacerItem6 = QtGui.QSpacerItem(196, 132, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout9.addItem(spacerItem6, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.gridlayout13 = QtGui.QGridLayout(self.tab_6)
        self.gridlayout13.setObjectName(_fromUtf8("gridlayout13"))
        self.groupBox_11 = QtGui.QGroupBox(self.tab_6)
        self.groupBox_11.setTitle(QtGui.QApplication.translate("CloudPage", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.gridlayout14 = QtGui.QGridLayout(self.groupBox_11)
        self.gridlayout14.setObjectName(_fromUtf8("gridlayout14"))
        self.label_9 = QtGui.QLabel(self.groupBox_11)
        self.label_9.setText(QtGui.QApplication.translate("CloudPage", "Identifier:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridlayout14.addWidget(self.label_9, 0, 0, 1, 1)
        self.lineEditNullIdentifer = QtGui.QLineEdit(self.groupBox_11)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditNullIdentifer.sizePolicy().hasHeightForWidth())
        self.lineEditNullIdentifer.setSizePolicy(sizePolicy)
        self.lineEditNullIdentifer.setObjectName(_fromUtf8("lineEditNullIdentifer"))
        self.gridlayout14.addWidget(self.lineEditNullIdentifer, 1, 0, 1, 1)
        self.gridlayout13.addWidget(self.groupBox_11, 0, 0, 1, 2)
        self.groupBox_10 = QtGui.QGroupBox(self.tab_6)
        self.groupBox_10.setTitle(QtGui.QApplication.translate("CloudPage", "NIOs", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.vboxlayout6 = QtGui.QVBoxLayout(self.groupBox_10)
        self.vboxlayout6.setObjectName(_fromUtf8("vboxlayout6"))
        self.listWidgetNull = QtGui.QListWidget(self.groupBox_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidgetNull.sizePolicy().hasHeightForWidth())
        self.listWidgetNull.setSizePolicy(sizePolicy)
        self.listWidgetNull.setObjectName(_fromUtf8("listWidgetNull"))
        self.vboxlayout6.addWidget(self.listWidgetNull)
        self.gridlayout13.addWidget(self.groupBox_10, 0, 2, 3, 1)
        self.pushButtonAddNull = QtGui.QPushButton(self.tab_6)
        self.pushButtonAddNull.setText(QtGui.QApplication.translate("CloudPage", "&Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonAddNull.setObjectName(_fromUtf8("pushButtonAddNull"))
        self.gridlayout13.addWidget(self.pushButtonAddNull, 1, 0, 1, 1)
        self.pushButtonDeleteNull = QtGui.QPushButton(self.tab_6)
        self.pushButtonDeleteNull.setEnabled(False)
        self.pushButtonDeleteNull.setText(QtGui.QApplication.translate("CloudPage", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonDeleteNull.setObjectName(_fromUtf8("pushButtonDeleteNull"))
        self.gridlayout13.addWidget(self.pushButtonDeleteNull, 1, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 261, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout13.addItem(spacerItem7, 2, 0, 2, 2)
        spacerItem8 = QtGui.QSpacerItem(20, 181, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout13.addItem(spacerItem8, 3, 2, 1, 1)
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.vboxlayout.addWidget(self.tabWidget)

        self.retranslateUi(CloudPage)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CloudPage)

    def retranslateUi(self, CloudPage):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("CloudPage", "NIO Ethernet", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("CloudPage", "NIO UDP", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("CloudPage", "NIO TAP", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("CloudPage", "NIO UNIX", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QtGui.QApplication.translate("CloudPage", "NIO VDE", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QtGui.QApplication.translate("CloudPage", "NIO NULL", None, QtGui.QApplication.UnicodeUTF8))

