'''
A "starting bag" is one which contains 3 items. We can use this so when we're building up bags
we don't start with a bag with a single present because that bag might not end up having 2 more
items added to bring it up to a minimum size.

Also, we don't want a "starting bag" to have something like 3 coals because such a bag is almost
certain to be invalid for being too heavy.

The sbags_dict property will be a dictionary with a key for each present and the value will be a list
of profiles. The largest present in a profile will match the key of the list it's in. This will be
used when looking for a starting bag with a present X - just use X as the key and go to that list
becaue we don't want to check for starting bags with presents bigger than X.
'''

import global_vars as gv
import bag_profile as bp
import profile_expected_weights as pew
import Expected_Weight as ew

class StartingBags:

    def setup(self):
        self.pew_cache = pew.ProfileExpectedWeights()
        self.sbags_dict = {} #a dictionary with a key for each present and the value will be a list of profiles
        for key_present in gv.presents_in_size_order:
            presents_in_order = [key_present]
            starting_bags_for_key = []
            self.add_bags_starting_with(starting_bags_for_key, presents_in_order)
            self.sbags_dict[key_present] = starting_bags_for_key

    #sbags_so_far is the list of all starting bags fopr the current key_present
    #presents_in_order is a list of presents (between 1 and 3) for which we have to consider extensions to reach the minimum bag size (3)
    def add_bags_starting_with(self, sbags_so_far, presents_in_order):
        if len(presents_in_order) == 3:
            sbag = self.presents_list_to_profile(presents_in_order)
            sbags_so_far.append(sbag)
            return
        #if we haven't return'ed then we need to consider recursively all extensions to presents_in_order involving ONLY PRESENTS SMALLER OR EQUAL TO the last present in presents_in_order
        last_present_in_list = presents_in_order[-1]
        presents_no_bigger = self.presents_not_bigger(last_present_in_list)
        for present_try_add in presents_no_bigger:
            #determine if we should add present_to_try_to_add to a bag which already has the presents in presents_in_order
            presents_in_order_profile = self.presents_list_to_profile(presents_in_order)
            extended_profile = presents_in_order_profile.addPresentCount(present_try_add, 1)
            #simply check if the expected weight (not setting to zero if under 3 presents or over 50 weight) is <= 50 ####################################################
            if presents_in_order_profile.try_improve_by_adding_present(present_try_add, self.pew_cache): #THIS IS WHERE IT CHECKS IF present_try_add COULD BE ADDED
                extended_presents_in_order = presents_in_order + [present_try_add]
                self.add_bags_starting_with(sbags_so_far, extended_presents_in_order)

    def presents_not_bigger(self, present):
        present_index = gv.presents_in_size_order.index(present)
        presents_in_size_order_last_index = len(gv.presents_in_size_order)
        return gv.presents_in_size_order[present_index:presents_in_size_order_last_index]

    def presents_list_to_profile(self, presents_list):
        prof = bp.Profile()
        for present in presents_list:
            prof.addPresentCount(present, 1)
        return prof

#Note on usage:
#sbags = StartingBags()
#sbags.setup()
#for keypresent in sbags.sbags_dict:
#    print "bags starting with: " + keypresent
#    baglist = sbags.sbags_dict[keypresent]
#    for bag in baglist:
#        print bag.presents
#        print "    [expected weight: " + str(ew.average_weight_over_x_simulations(gv.default_simulations, bag)) + "]"


