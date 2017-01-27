import global_vars as gv
#import Expected_Weight as ew
import bag_profile as bp
import PresentsToDistribute as pd
import profile_expected_weights as pew

#setup the variables we'll need throughout the algorithm
bag_profiles = []
presents_left = pd.PresentsToDistribute()
ew_cache = pew.ProfileExpectedWeights()

for present in gv.presents_in_size_order:
    #keep adding this present to bags in bag_profiles until either we have 1000 bags and can't fit present into any
    #or presentsLeft runs out of this present

    print "*********** starting present: " + present

    stop_now = False

    while not stop_now:
        presents_left.take_present(present) #remove a present from the presents_left list and try to add it to a bag/profile
        added_ok = False
        for profile in bag_profiles:
            added_ok = profile.try_improve_by_adding_present(present, ew_cache)
            if added_ok:
                break #exits the for loop early because we've found a bag to dd this present to
        num_bag_profiles = len(bag_profiles)
        if (not added_ok) and (num_bag_profiles < 1000):
            new_profile = bp.Profile()
            new_profile.addPresentCount(present, 1)
            bag_profiles.append(new_profile)
            print "new bag created (" + str(len(bag_profiles)) + " bags now)"
            added_ok = True
        stop_now = (not added_ok) or (presents_left.count_left(present) <= 0)

#OK, I think bag_profiles should now be a solution
print "Bags count at end: " + str(len(bag_profiles))

