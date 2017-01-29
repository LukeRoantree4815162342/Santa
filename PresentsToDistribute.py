import global_vars as gv

class PresentsToDistribute:
    def __init__(self):
        self.remaining_dict = {}
        self.remaining_dict[gv.ball] = 500
        self.remaining_dict[gv.bike] = 1000
        self.remaining_dict[gv.blocks] = 1000
        self.remaining_dict[gv.book] = 200
        self.remaining_dict[gv.coal] = 166
        self.remaining_dict[gv.doll] = 1000
        self.remaining_dict[gv.gloves] = 1200
        self.remaining_dict[gv.horse] = 1100
        self.remaining_dict[gv.train] = 1000

#    def take_present(self, present):
#        self.remaining_dict[present] -= 1

    def try_take_present(self, present):
        if(self.count_left > 0):
            self.remaining_dict[present] -= 1
            return True
        else:
            return False

    def count_left(self, present):
        return  self.remaining_dict[present]

    def can_profile_be_taken(self, prof):
        prof_presents = prof.presents
        profile_can_be_filled_so_far = True
        for present, count in prof.presents.iteritems():
            if self.remaining_dict[present] < count:
                profile_can_be_filled_so_far = False
                break
        return profile_can_be_filled_so_far

    def take_profile(self, prof):
        for present, count in prof.presents.iteritems():
            self.remaining_dict[present] -= count

#test
#ptd = PresentsToDistribute()
#print ptd.count_left(gv.horse)
#ptd.take_present(gv.horse)
#print ptd.count_left(gv.horse)
#ptd.take_present(gv.book)
#print ptd.count_left(gv.book)
#print ptd.count_left(gv.horse)
