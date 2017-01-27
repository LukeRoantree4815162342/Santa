'''
A bag profile is simply a description of the presents in a bag without the suffixes ( _324). It
simply keeps track of how many of each present is in the bag.  Each profile has an associated key,
e.g. ball#1+bike#3+gloves#2
The present names are always in alpha order in the key so two profiles with the same number of each
present will always have the same key.

Use the present variables in global_vars when adding to Profile objects
'''

import collections as cl
import global_vars as gv
#import gift_ids as gi
#import profile_expected_weights as pew

class Profile:
    def __init__(self):
        self.presents = cl.Counter()

    def key(self):
        pkey = ""
        pkey_empty = True
        for present in gv.presents_in_alpha_order:
            present_count_in_profile = self.presents[present]
            if present_count_in_profile > 0:
                if not pkey_empty:
                    pkey += "+"
                pkey_empty = False
                pkey += present + "#" + str(present_count_in_profile)
        return pkey

    def addPresentCount(self, present, count):
        c = cl.Counter()
        c[present] = count
        self.presents = self.presents + c

    def subtractPresentCount(self, present, count):
        c = cl.Counter()
        c[present] = count
        self.presents.subtract(c)

    def line_for_csv(self, gift_id_generator):
        line = ""
        first_present = True
        for present in gv.presents_in_alpha_order:
            present_count_in_profile = self.presents[present]
            for i in range(present_count_in_profile):
                gift_id = gift_id_generator.get_present_id_and_incerment(present)
                if not first_present:
                    line += ", "
                first_present = False
                line += present + "_" + str(gift_id)
        return line

    def try_improve_by_adding_present(self, present, ew_cache):
        curr_weight = ew_cache.get_profile_weight(self)
        self.addPresentCount(present, 1)
        new_weight = ew_cache.get_profile_weight(self)
        if new_weight > curr_weight:
            return True
        else:
            self.subtractPresentCount(present, 1)
            return False

#test
#p = Profile()
#ew_cache = pew.ProfileExpectedWeights()
#p.addPresentCount(gv.horse, 3)
#p.addPresentCount(gv.book, 1)
#print p.presents
#print p.key()
#g = gi.GiftIDs()
#print p.line_for_csv(g)
#print "Trying to add coal..."
#added_ok = p.try_improve_by_adding_present(gv.coal, ew_cache)
#print added_ok
#print p.presents
#print "Trying to add coal again..."
#added_ok = p.try_improve_by_adding_present(gv.coal, ew_cache)
#print added_ok
#print p.presents
