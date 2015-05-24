# !/usr/bin/env python
# -*- coding:  utf-8 -*-

from PyQt4.QtCore import QUrl


class ObjectUrl():

   def __init__(self):
      self.url = QUrl('http://www.google.com')

   def update_url(self, new_url):
      if not new_url.startswith('http://'):
         new_url = 'http://' + new_url
      
      self.url = QUrl(new_url)

   def get_url(self):
      return self.url
