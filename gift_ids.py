import global_vars as gv

class GiftIDs:
    def __init__(self):
        self.id_dict = {}
        for present in gv.presents_in_alpha_order:
            self.id_dict[present] = 0

    #returns the
    def get_present_id_and_incerment(self, present):
        current_id = self.id_dict[present];
        self.id_dict[present] += 1
        return current_id


#test
#g = GiftIDs()
#print g.get_present_id_and_incerment(gv.horse)
#print g.get_present_id_and_incerment(gv.book)
#print g.get_present_id_and_incerment(gv.horse)
#print g.get_present_id_and_incerment(gv.coal)
#print g.get_present_id_and_incerment(gv.horse)