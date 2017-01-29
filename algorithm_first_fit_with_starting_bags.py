import global_vars as gv
#import Expected_Weight as ew
import bag_profile as bp
import PresentsToDistribute as pd
import profile_expected_weights as pew
import starting_bags as sb
import gift_ids as gi

#This algorithm is the same as Firat Fit except instead of putting the next present i its own bag when it won't fit into any existing bags,
#   it picks one of the starting bags (containing that next present).

#setup the variables we'll need throughout the algorithm
bag_profiles = []
presents_left = pd.PresentsToDistribute()
ew_cache = pew.ProfileExpectedWeights()

sbags = sb.StartingBags()
sbags.setup()

for present in gv.presents_in_size_order:
    #keep adding this present to bags in bag_profiles until either we have 1000 bags and can't fit present into any
    #or presentsLeft runs out of this present

    print "*********** starting present: " + present + ", num left: " + str(presents_left.count_left(present))

    stop_now = presents_left.count_left(present) <= 0

    while not stop_now:
        added_ok = False
        for profile in bag_profiles:
            added_ok = profile.try_improve_by_adding_present(present, ew_cache)
            if added_ok:
                presents_left.try_take_present(present)
                break #exits the for loop early because we've found a bag to dd this present to
        num_bag_profiles = len(bag_profiles)
        if (not added_ok) and (num_bag_profiles < 1000):
            #Pick the best starting bag from those with key = present
            possible_start_bags = sbags.sbags_dict[present]
            for sbag_profile in possible_start_bags:
                if presents_left.can_profile_be_taken(sbag_profile):
                    presents_left.take_profile(sbag_profile)
                    bag_profiles.append(sbag_profile)
                    added_ok = True
                    break
        stop_now = (not added_ok) or (presents_left.count_left(present) <= 0)

#OK, I think bag_profiles should now be a solution
#print "Bags count at end: " + str(len(bag_profiles))

g = gi.GiftIDs()
f = open('affsb.txt', 'w')
f.write("Gifts\n")
for profile in bag_profiles:
    expweight = ew_cache.get_profile_weight(profile)
    f.write(profile.line_for_csv(g) + "\n")
f.close()