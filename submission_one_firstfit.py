# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 23:45:30 2017

@author: Luke
"""

import numpy as np
import csv
import os

script_dir = os.path.dirname(__file__)
gifts_csv_location = os.path.join(script_dir, "giftsdata.csv")
gifts = open(gifts_csv_location, 'r')
gifts = gifts.read()
gifts = gifts.split('\n')

submission_one_csv = open("possible_submission_bagsof7b.csv", 'wb')
np.random.shuffle(gifts)

writer = csv.writer(submission_one_csv, quoting=csv.QUOTE_NONNUMERIC)
row1 = []
row1.append('Gifts')
writer.writerow(row1)
bagsize = 7
for i in range(len(gifts)/bagsize -25): #25 is specific to bagsize of 7; makes it 25 over limit
    row = []
    row.append('')
    for j in range(0,9):
        if j<9:
            row[0] = ''.join([row[0],gifts[bagsize*i+j], ' '])
        else:
            row[0] = ''.join([row[0],gifts[bagsize*i+j]])
    writer.writerow(row)
submission_one_csv.close()

