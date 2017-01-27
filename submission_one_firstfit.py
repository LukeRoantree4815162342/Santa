# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 23:45:30 2017

@author: Luke
"""

import numpy as np
import csv
import os
import global_vars as gv
import gift_ids as gi
import bag_profile as bp
import algorithm_first_fit as aff

g = gi.GiftIDs()

#script_dir = os.path.dirname(__file__)
#gifts_csv_location = os.path.join(script_dir, "giftsdata.csv")
#gifts = open(gifts_csv_location, 'r')
#gifts = gifts.read()
#gifts = gifts.split('\n')

submission_one_csv = open("dadtest.csv", 'wb')
#np.random.shuffle(gifts)

writer = csv.writer(submission_one_csv, quoting=csv.QUOTE_NONNUMERIC)
row1 = []
row1.append('Gifts')
writer.writerow(row1)
#bagsize = 7
dad_array = aff.bag_profiles
for i in dad_array: #25 is specific to bagsize of 7; makes it 25 over limit
    row = []
    row.append('')
    row[0] = ''.join([row[0],str(i.line_for_csv(g))])
    writer.writerow(row)
submission_one_csv.close()
#
#
#for i in range(len(dad_array)): #25 is specific to bagsize of 7; makes it 25 over limit
#    row = []
#    row.append('')
#    for j in range(0,9):
#        row[0] = ''.join([row[0], dad_array])
#    writer.writerow(row)
#submission_one_csv.close()

