#This is quickie code - almost no testing for problems. Doesn't check there are not too many of
#any one type of present or that the number suffix of a present is not used twice.

import numpy as np
import global_vars as gv
def gen_prob_wt(present):
    #present should be one of "blocks", "gloves", "doll" etc.
    present = present.lower()
    if present == gv.horse:
        return max(0, np.random.normal(5, 2, 1)[0])
    elif present == gv.ball:
        return max(0, 1 + np.random.normal(1, 0.3, 1)[0])
    elif present == gv.bike:
        return max(0, np.random.normal(20, 10, 1)[0])
    elif present == gv.train:
        return max(0, np.random.normal(10, 5, 1)[0])
    elif present == gv.coal:
        return 47 * np.random.beta(0.5, 0.5, 1)[0]
    elif present == gv.book:
        return np.random.chisquare(2, 1)[0]
    elif present == gv.doll:
        return np.random.gamma(5, 1, 1)[0]
    elif present == gv.blocks:
        return np.random.triangular(5, 10, 20, 1)[0]
    elif present == gv.gloves:
        return 3.0 + np.random.rand(1)[0] if np.random.rand(1) < 0.3 else np.random.rand(1)[0]
    else:
        return 'error' #this shouldn't happen - an unknown present
                       #updated by luke to return a string so it crashes rather than not showing a problem if one exists
#END: def genProbWt

def try_eval_bag(bag_line):
    bag_results = {}
    bag_results["bagwt"] = 0
    bag_results["tooheavy"] = False
    bag_results["toosmall"] = False
    bag_results["valid"] = False #this will be set to True once we can confirm that the bag is not overfilled
    presents = bag_line.split(' ')
    present_count_so_far = 0
    bag_wt_so_far = 0.0
    for present in presents:
        present = present.strip(" _0123456789") #we should be left with only "blocks", "gloves", "doll", etc.
        if len(present) == 0:
            continue
        present_count_so_far += 1
        present_wt = gen_prob_wt(present)
        bag_wt_so_far += present_wt

    if (bag_wt_so_far > 50.0):
        bag_results["bagwt"] = 0
        bag_results["tooheavy"] = True
        bag_results["valid"] = False
    elif (present_count_so_far < 3):
        bag_results["bagwt"] = 0     #it doesn't matter what we set the bagwt to if the bag is not valid
        bag_results["toosmall"] = True
        bag_results["valid"] = False
    else:
        bag_results["bagwt"] = bag_wt_so_far     #it doesn't matter what we set the bagwt to if the bag is not valid
        bag_results["valid"] = True

    return bag_results
#END: def try_eval_bag
    
def try_eval_bag_array(bag_line):
    bag_results = {}
    bag_results["bagwt"] = 0
    bag_results["valid"] = False #this will be set to True once we can confirm that the bag is not overfilled

    presents = bag_line
    present_count_so_far = 0
    bag_wt_so_far = 0.0
    for present in presents:
        if len(present) == 0:
            continue
        present_count_so_far += 1
        present_wt = gen_prob_wt(present)
        bag_wt_so_far += present_wt

    if (present_count_so_far < 3) or (bag_wt_so_far > 50.0):
        bag_results["bagwt"] = 0     #it doesn't matter what we set the bagwt to if the bag is not valid
        bag_results["valid"] = False
    else:
        bag_results["bagwt"] = bag_wt_so_far     #it doesn't matter what we set the bagwt to if the bag is not valid
        bag_results["valid"] = True

    return bag_results


def try_eval(submission_text):
    subm_results = {}
    subm_results["totwt"] = 0
    subm_results["numvalidbags"] = 0
    subm_results["numinvalidbags"] = 0
    subm_results["numtooheavy"] = 0
    subm_results["numtoosmall"] = 0
    subm_results["totwaste"] = 0.0 #tot wt wasted among valid bags
    subm_results["avgwaste"] = 0.0 #avg wt wasted among valid bags
    #subm_results["avgnumtooheavy"] = 0.0

    bagLines = submission_text.splitlines()

    for bag_line in bagLines:
        bag_line = bag_line.strip()
        if (len(bag_line) == 0) or (bag_line == "Gifts"):
            continue  # skip empty lines and the first line
        bag_results = {}
        bag_results = try_eval_bag(bag_line)
        if bag_results["valid"]:
            subm_results["totwt"] += bag_results["bagwt"]
            subm_results["numvalidbags"] += 1
            subm_results["totwaste"] += (50.0 - bag_results["bagwt"])
        elif bag_results["tooheavy"]:
            subm_results["numinvalidbags"] += 1
            subm_results["numtooheavy"] += 1
        else: #too small
            subm_results["numinvalidbags"] += 1
            subm_results["numtoosmall"] += 1

    if subm_results["numvalidbags"] == 0:
        subm_results["avgwaste"] = 0.0  # Should this not be 50.0? -Luke
    else:
        subm_results["avgwaste"] = float(subm_results["totwaste"]) / float(subm_results["numvalidbags"])
        #subm_results["avgnumtooheavy"] = float(subm_results["numtooheavy"]) / float(len(bagLines))
    return subm_results
#END: def try_eval

def try_eval_multiple(submission_text, multiple):
    multiple_results = {}
    multiple_results["multipletotwt"] = 0
    multiple_results["multiplenumvalidbags"] = 0
    multiple_results["multiplenuminvalidbags"] = 0
    multiple_results["multipleavgwaste"] = 0.0
    multiple_results["multiplenumtooheavy"] = 0.0
    multiple_results["multiplenumtoosmall"] = 0.0

    for submIndex in range(multiple):
        subm_results = try_eval(submission_text)
        multiple_results["multipletotwt"] += subm_results["totwt"]
        multiple_results["multiplenumvalidbags"] += subm_results["numvalidbags"]
        multiple_results["multiplenuminvalidbags"] += subm_results["numinvalidbags"]
        multiple_results["multipleavgwaste"] += subm_results["avgwaste"]
        multiple_results["multiplenumtooheavy"] += subm_results["numtooheavy"]
        multiple_results["multiplenumtoosmall"] += subm_results["numtoosmall"]

    multiple_results["avgtotwt"] = float(multiple_results["multipletotwt"]) / float(multiple)
    multiple_results["avgnumvalidbags"] = float(multiple_results["multiplenumvalidbags"]) / float(multiple)
    multiple_results["avgnuminvalidbags"] = float(multiple_results["multiplenuminvalidbags"]) / float(multiple)
    multiple_results["avgwaste"] = float(multiple_results["multipleavgwaste"]) / float(multiple)
    multiple_results["avgnumtooheavy"] = float(multiple_results["multiplenumtooheavy"]) / float(multiple)
    multiple_results["avgnumtoosmall"] = float(multiple_results["multiplenumtoosmall"]) / float(multiple)


    #we only need to keep the "avgXXX" properties of the multiple_results dictionary
    del multiple_results["multipletotwt"]
    del multiple_results["multiplenumvalidbags"]
    del multiple_results["multiplenuminvalidbags"]
    del multiple_results["multipleavgwaste"]
    del multiple_results["multiplenumtooheavy"]
    del multiple_results["multiplenumtoosmall"]

    return multiple_results
#END: def try_eval_multiple


#TEST:
#Note: In the sample submission there are 716 bags
#
#submfile = open("affsb.csv", "r")
#submission_text = submfile.read()
#multiple_results = try_eval_multiple(submission_text, 500)
#print multiple_results["avgnumvalidbags"]+multiple_results["avgnuminvalidbags"]
#for key in multiple_results:
#    print key, multiple_results[key]

'''
Donal tested the above (test code commented out above) doing two
"Runs" of 500 multiples each (to get reliable averages) using the
sample submission file.

Here are the results:
using 500 runs:
avgnumvalidbags 451.362
avgwaste 29.0612712012
avgnuminvalidbags 264.638
avgtotwt 9453.42666807

using 500 runs:
avgnumvalidbags 451.044
avgwaste 29.097409031
avgnuminvalidbags 264.956
avgtotwt 9430.60693972

So, reasonably close agreement. Also notice how awful the sample submission is!
'''

