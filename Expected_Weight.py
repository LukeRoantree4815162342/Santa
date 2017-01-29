# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 21:56:08 2017

@author: Luke
"""

import TryEval
import numpy as np
import global_vars as gv
import bag_profile as bp


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
    running_total_score = running_total_score if (running_total_score<50.0) else 0.0
    #print running_total_score
    return running_total_score
    

def average_weight_over_x_simulations(x, profile):
    running_total_score = 0
    for i in range(x):
        running_total_score += get_weight_of_profile_once(profile)
    return 1.0*running_total_score/(1.0*x)


#print average_weight_over_x_simulations(100000, example_profile)

#p = bp.Profile()
#p.addPresentCount(gv.horse, 2)
#print p.presents
#print average_weight_over_x_simulations(1000, p)
#for i in range(15):
#    p.addPresentCount(gv.horse, 1)
#    print p.presents
#    print average_weight_over_x_simulations(100, p)

#chrissy line: doll_13 doll_14 ball_23 doll_15 horse_19 train_12 ball_24 book_23 gloves_21 ball_25
#p = bp.Profile()
#p.addPresentCount(gv.doll, 3)
#p.addPresentCount(gv.ball, 2)
#p.addPresentCount(gv.horse, 1)
#p.addPresentCount(gv.train, 1)
#p.addPresentCount(gv.book, 1)
#p.addPresentCount(gv.gloves, 1)
#print p.presents
#print average_weight_over_x_simulations(1000, p)

#p = bp.Profile()
#p.addPresentCount(gv.bike, 1)
#p.addPresentCount(gv.blocks, 1)
#p.addPresentCount(gv.horse, 2)
#print p.presents
#print "weight: " + str(average_weight_over_x_simulations(100, p))
#p.addPresentCount(gv.gloves, 1)
#print p.presents
#print "weight: " + str(average_weight_over_x_simulations(100, p))
