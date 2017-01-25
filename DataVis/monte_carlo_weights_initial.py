# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 15:55:06 2017

@author: Luke
"""

import numpy as np
import bar_chart_of_categories as barc
import matplotlib.pyplot as plt

def horse():
    return max(0, np.random.normal(5,2,1)[0])

def ball():
    return max(0, 1 + np.random.normal(1,0.3,1)[0])

def bike():
    return max(0, np.random.normal(20,10,1)[0])

def train():
    return max(0, np.random.normal(10,5,1)[0])

def coal():
    return 47 * np.random.beta(0.5,0.5,1)[0]

def book():
    return np.random.chisquare(2,1)[0]

def doll():
    return np.random.gamma(5,1,1)[0]

def blocks():
    return np.random.triangular(5,10,20,1)[0]

def gloves():
    return 3.0 + np.random.rand(1)[0] if np.random.rand(1) < 0.3 else np.random.rand(1)[0]
    
presents_with_random_weights = {}

del barc.categories[-1] # removes the '' element from categories
del barc.counts['']     #removes it from counts dictionary

for simulation_count in range(1000):
    for i in barc.categories:
        if not i in presents_with_random_weights:
            presents_with_random_weights[i] = []
        for j in range(barc.counts[i]):
            presents_with_random_weights[i].append(locals()[i]())
            
for present in presents_with_random_weights:
    new_hist = plt.figure(present)
    plt.hist(presents_with_random_weights[present], 300, label=str(present))
    plt.xlabel('weight')


    