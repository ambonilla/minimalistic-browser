# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'browser.ui'
#
# Created: Sat May 23 16:05:48 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Browser(object):
    def setupUi(self, Browser):
        Browser.setObjectName(_fromUtf8("Browser"))
        Browser.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Browser.sizePolicy().hasHeightForWidth())
        Browser.setSizePolicy(sizePolicy)
        self.centralWidget = QtGui.QWidget(Browser)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(1, -1, 1, -1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.back_button = QtGui.QPushButton(self.centralWidget)
        self.back_button.setMaximumSize(QtCore.QSize(32, 32))
        self.back_button.setText(_fromUtf8(""))
        self.back_button.setObjectName(_fromUtf8("back_button"))
        self.gridLayout.addWidget(self.back_button, 0, 0, 1, 1)
        self.forward_button = QtGui.QPushButton(self.centralWidget)
        self.forward_button.setMaximumSize(QtCore.QSize(32, 32))
        self.forward_button.setText(_fromUtf8(""))
        self.forward_button.setObjectName(_fromUtf8("forward_button"))
        self.gridLayout.addWidget(self.forward_button, 0, 1, 1, 1)
        self.url_bar = QtGui.QLineEdit(self.centralWidget)
        self.url_bar.setObjectName(_fromUtf8("url_bar"))
        self.gridLayout.addWidget(self.url_bar, 0, 3, 1, 1)
        self.reload_button = QtGui.QPushButton(self.centralWidget)
        self.reload_button.setMaximumSize(QtCore.QSize(32, 32))
        self.reload_button.setText(_fromUtf8(""))
        self.reload_button.setObjectName(_fromUtf8("reload_button"))
        self.gridLayout.addWidget(self.reload_button, 0, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.tab_widget = QtGui.QTabWidget(self.centralWidget)
        self.tab_widget.setObjectName(_fromUtf8("tab_widget"))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.web_view = QtWebKit.QWebView(self.tab1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.web_view.sizePolicy().hasHeightForWidth())
        self.web_view.setSizePolicy(sizePolicy)
        self.web_view.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.UnitedStates))
        self.web_view.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.web_view.setObjectName(_fromUtf8("web_view"))
        self.verticalLayout.addWidget(self.web_view)
        self.tab_widget.addTab(self.tab1, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tab_widget)
        Browser.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Browser)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        Browser.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(Browser)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        Browser.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(Browser)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        Browser.setStatusBar(self.statusBar)

        self.retranslateUi(Browser)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Browser)
        Browser.setTabOrder(self.web_view, self.back_button)
        Browser.setTabOrder(self.back_button, self.forward_button)
        Browser.setTabOrder(self.forward_button, self.reload_button)
        Browser.setTabOrder(self.reload_button, self.url_bar)
        Browser.setTabOrder(self.url_bar, self.tab_widget)

    def retranslateUi(self, Browser):
        Browser.setWindowTitle(_translate("Browser", "Navegador Minimalista", None))

from PyQt4 import QtWebKit
