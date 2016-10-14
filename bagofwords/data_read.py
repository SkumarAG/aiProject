from pandas import read_csv
from collections import OrderedDict
import re,itertools
def dataRead():
  tweet_data = read_csv(filepath_or_buffer ="C:/Users/Ramanuja/Desktop/data2.csv",header=None,usecols = [9])# since no header info
  return tweet_data
