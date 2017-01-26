'''
A bag profile is simply a description of the presents in a bag without the suffixes ( _324). It
simply keeps track of how many of each present is in the bag.  Each profile has an associated key,
e.g. ball#1+bike#3+gloves#2
The present names are always in alpha order in the key so two profiles with the same number of each
present will always have the same key.
The present spellings are (exactly):

ball
bike
blocks
book
coal
doll
gloves
horse
train
'''

import collections as cl
import global_vars as gv

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
