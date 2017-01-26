# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 21:56:08 2017

@author: Luke
"""

import TryEval
import numpy as np
import global_vars as gv


#
#def get_weight_of_profile_once(profile):
#    gifts_grouped = profile.split('+')
#    gifts = []
#    for gift_type in gifts_grouped:
#        gifts_of_type = [gift_type.split('#')[0]]*int(gift_type.split('#')[1])
#        gifts.extend(gifts_of_type)
#    weight_once = TryEval.try_eval_bag_array(gifts)
#    return weight_once
#    


def get_weight_of_profile_once(profile):
    running_total_score = 0
    for present in gv.presents_in_alpha_order:
        present_count_in_profile = profile.presents[present]
        for i in range(present_count_in_profile):
            running_total_score += TryEval.gen_prob_wt(present)
    return running_total_score
    

def average_weight_over_x_simulations(x, profile):
    running_total_score = 0
    for i in range(x):
        sim_score = get_weight_of_profile_once(profile)
        running_total_score+= sim_score['bagwt']
    return 1.0*running_total_score/(1.0*x)

print average_weight_over_x_simulations(100000, example_profile)