# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 15:51:17 2016

@author: Ramanuja
"""

from pandas import read_csv
from collections import OrderedDict
import re,itertools
tweet_data = read_csv(filepath_or_buffer ="C:/Users/Ramanuja/Desktop/data2.csv",header=None,usecols = [9])# since no header info

