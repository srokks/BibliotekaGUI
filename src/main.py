'''
Created on 23 sty 2014

@author: Srokks
'''
# -*- coding: utf-8 -*-

from bibliotekav0 import Biblioteka as bibl
from biblioteka import Biblioteka as bibla
import datetime

today = datetime.datetime.now()
print int(datetime.date.today().strftime("%j"))
print datetime.date.today().strftime("%Y")