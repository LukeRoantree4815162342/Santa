# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 23:45:30 2017

@author: Luke
"""

import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#import random
import csv
#import seaborn as sb
import os

script_dir = os.path.dirname(__file__)
gifts_csv_location = os.path.join(script_dir, "../giftsdata.csv")
gifts = open(gifts_csv_location, 'r')
gifts = gifts.read()
gifts = gifts.split('\n')
#print gifts
submission_one_csv = open("giftsdata.csv", 'wt')
np.random.shuffle(gifts)
#print gifts
#submission_one_csv.write()

#print gifts[3+7]
#print gifts[1]
#
writer = csv.writer(submission_one_csv, quoting=csv.QUOTE_NONNUMERIC)
for i in range(len(gifts)/10):
    row = []
    row.append('')
    for j in range(0,9):
        row[0] = ''.join([row[0],gifts[i+j], ' '])
#        print row[0]
	#print gifts[i+j]
#    row[0] = ' '.join(row[0])
#    #print row
#    row = tuple(row)
    writer.writerow(row)
submission_one_csv.close()
#

#print open("giftsdata.csv", 'rt').read()
#submission_one_csv = ''
#for i in range(len(gifts)/10):
#    for j in range(0,9):
#        submission_one_csv += gifts[i+j] + ' '
#    submission_one_csv += ','
#submission_one_csv.close()

