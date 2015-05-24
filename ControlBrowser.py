# !/usr/bin/env python
# -*- coding:  utf-8 -*-

"""
ControlBrowser.py

Author: Adrian Bonilla @_ambonilla
2015

"""

from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QPixmap

from PyQt4.QtCore import QUrl

from ViewBrowser import Ui_Browser
from ModelBrowser import ObjectUrl

import sys

class WebBrowser(QMainWindow):

   def __init__(self):
      super(WebBrowser, self).__init__()
      self.ui = Ui_Browser()
      self.ui.setupUi(self)
      self.url_object = ObjectUrl()
      self.setup_gui()

   #GUI Setup

   def setup_gui(self):
      self.setup_buttons()
      self.setup_browser()
      self.default_tab()
      
   #Buttons & Connect Actions 

   def setup_buttons(self):
      self.ui.back_button.clicked.connect(self.back_page)
      self.ui.forward_button.clicked.connect(self.forward_page)
      self.ui.reload_button.clicked.connect(self.reload_page)

      self.ui.back_button.setIcon(QIcon(QPixmap("img/back.png")))
      self.ui.forward_button.setIcon(QIcon(QPixmap("img/forward.png")))
      self.ui.reload_button.setIcon(QIcon(QPixmap("img/reload.png")))

   def setup_browser(self):
      self.ui.web_view.loadFinished.connect(self.update_tab)
      self.ui.web_view.titleChanged.connect(self.update_tab_name)
      self.ui.web_view.urlChanged.connect(self.update_url_bar)
      self.ui.url_bar.returnPressed.connect(self.open_url)


   #Functions

   def back_page(self):
      self.ui.web_view.back()

   def forward_page(self):
      self.ui.web_view.forward()

   def reload_page(self):
      self.ui.web_view.reload()

   def default_tab(self):
      self.ui.web_view.load(self.url_object.get_url())

   def update_tab(self, result):
      if result:
         self.ui.tab_widget.setTabText(0,self.get_string(self.ui.web_view.title()))
      else:
         self.ui.tab_widget.setTabText(0, "Error")

   def update_tab_name(self, name):
      self.ui.tab_widget.setTabText(0,self.get_string(name))

   def update_url_bar(self, new_url=None):
      if new_url:
         self.ui.url_bar.setText(new_url.toString())

   def open_url(self):
      new_url = self.get_string(self.ui.url_bar.text())
      self.url_object.update_url(new_url)
      self.default_tab()


   def get_string(self, string):
      output = unicode(string.toUtf8(),"utf-8")
      return output.strip()       




def main():
   app = QApplication(sys.argv)
   new_browser = WebBrowser()
   new_browser.show()
   sys.exit(app.exec_())

if __name__ == "__main__":
   main()

