#import bag_profile as bp
import Expected_Weight as ew
import global_vars as gv


class ProfileExpectedWeights:
    def __init__(self):
        self.weights_cache = {}

    def get_profile_weight(self, profile):
        pkey = profile.key()
        if not (pkey in self.weights_cache):
            weight = ew.average_weight_over_x_simulations(gv.default_simulations, profile)
            self.weights_cache[pkey] = weight
        return self.weights_cache[pkey]

    def cache_count(self):
        return len(self.weights_cache)

#test
#p = bp.Profile()
#p.addPresentCount(gv.horse, 3)
#p.addPresentCount(gv.book, 1)
#pew = ProfileExpectedWeights()
#print "Cache size: " + str(pew.cache_count())
#weight = pew.get_profile_weight(p)
#print "Cache size: " + str(pew.cache_count())
#weight = pew.get_profile_weight(p)
#print "Cache size: " + str(pew.cache_count())
#p.addPresentCount(gv.book, 1)
#weight = pew.get_profile_weight(p)
#print "Cache size: " + str(pew.cache_count())
