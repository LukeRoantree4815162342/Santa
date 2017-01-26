# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 21:56:08 2017

@author: Luke
"""

import TryEval
import numpy as np

example_profile = 'ball#2+bike#2+gloves#1'

def get_weight_of_profile_once(profile):
    gifts_grouped = profile.split('+')
    gifts = []
    for gift_type in gifts_grouped:
        gifts_of_type = [gift_type.split('#')[0]]*int(gift_type.split('#')[1])
        gifts.extend(gifts_of_type)
    weight_once = TryEval.try_eval_bag_array(gifts)
    return weight_once
    

def average_weight_over_x_simulations(x, profile):
    running_total_score = 0
    for i in range(x):
        sim_score = get_weight_of_profile_once(profile)
        running_total_score+= sim_score['bagwt']
    return 1.0*running_total_score/(1.0*x)

print average_weight_over_x_simulations(100000, example_profile)