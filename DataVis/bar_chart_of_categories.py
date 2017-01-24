# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 23:25:19 2017

@author: Luke
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import os

script_dir = os.path.dirname(__file__)
gifts_csv_location = os.path.join(script_dir, "../giftsdata.csv")
gifts = open(gifts_csv_location, 'r')
gifts = gifts.read()
gifts = gifts.split('\n')

categories = []
counts = {}
def categorise(gift):
    gift = gift.split('_')
    gift = gift[0]
    if gift in categories:
        counts[gift]+=1
    else:
        categories.append(gift)
        counts[gift]=1

for i in range(1,len(gifts)):
    categorise(gifts[i])
#   print counts

temp = []
for i in categories:
    temp.append(counts[i])
x = plt.bar(np.arange(len(categories)), temp, 0.35, label='categories')
plt.xlabel('categories')
plt.ylabel('counts')
plt.xticks(np.arange(len(categories)) + 0.35 / 2, categories)
plt.show()

    