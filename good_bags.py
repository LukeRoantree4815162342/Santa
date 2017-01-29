#function to generate a sorted list of all "good" bags, i.e. bags for which it is not beneficial (gives higher expeted weight) to omit any present in the bag.
import global_vars as gv
import bag_profile as bp
import profile_expected_weights as pew
import Expected_Weight as ew

class GoodBags:

    def setup(self):
        self.pew_cache = pew.ProfileExpectedWeights()

        #one-off build up a dictionary of list of all perents no bigger than the key present
        self.presents_not_bigger = {}
        for present in gv.presents_in_size_order:
            presents_no_bigger = self.presents_not_bigger_than(present)
            self.presents_not_bigger[present] = presents_no_bigger

        self.goodbags = [] #the elements will be dictionaries with a profile and a expwt

        currbag = bp.Profile()
        biggest_present = gv.presents_in_size_order[0]
        self.add_bags_with_base(currbag, biggest_present)

        #sort the bags in reverse order of expwt
        self.goodbags.sort(key=lambda x: x["expwt"], reverse=True)

    def add_bags_with_base(self, currbag, present_no_bigger):
        global f
        presents_no_bigger = self.presents_not_bigger[present_no_bigger]
        for pres in presents_no_bigger:
            #consider adding pres to currbag
            copy_currbag = currbag.clone()
            if copy_currbag.try_improve_by_adding_present(pres, self.pew_cache):
                copy_currbag_wt = self.pew_cache.get_profile_weight(copy_currbag)
                self.goodbags.append({"profile": copy_currbag, "expwt": copy_currbag_wt})
                print copy_currbag.presents, "  wt=" + str(copy_currbag_wt)
                self.add_bags_with_base(copy_currbag, pres)

    def presents_not_bigger_than(self, present):
        present_index = gv.presents_in_size_order.index(present)
        presents_in_size_order_last_index = len(gv.presents_in_size_order) - 1
        return gv.presents_in_size_order[present_index:presents_in_size_order_last_index + 1]

#test

#f = open('goodbags_results.txt', 'w')

gbags= GoodBags()
gbags.setup()
print "All good bags:"
for gbag in gbags.goodbags:
    print gbag["profile"].presents
    print gbag["expwt"]

#f.close()

