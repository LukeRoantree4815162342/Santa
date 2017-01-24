#This is quickie code - almost no testing for problems. Doesn't check there are not too many of
#any one type of present or that the number suffix of a present is not used twice.

import numpy as np

def genProbWt(present):
    #present should be one of "blocks", "gloves", "doll" etc.
    present = present.lower()
    if present == "horse":
        return max(0, np.random.normal(5, 2, 1)[0])
    elif present == "ball":
        return max(0, 1 + np.random.normal(1, 0.3, 1)[0])
    elif present == "bike":
        return max(0, np.random.normal(20, 10, 1)[0])
    elif present == "train":
        return max(0, np.random.normal(10, 5, 1)[0])
    elif present == "coal":
        return 47 * np.random.beta(0.5, 0.5, 1)[0]
    elif present == "book":
        return np.random.chisquare(2, 1)[0]
    elif present == "doll":
        return np.random.gamma(5, 1, 1)[0]
    elif present == "block":
        return np.random.triangular(5, 10, 20, 1)[0]
    elif present == "gloves":
        return 3.0 + np.random.rand(1)[0] if np.random.rand(1) < 0.3 else np.random.rand(1)[0]
    else:
        return 0.0 #this shouldn't happen - an unknown present
#END: def genProbWt

def TryEvalBag(bagLine):
    bagResults = {}
    bagResults["bagwt"] = 0
    bagResults["valid"] = False #this will be set to True once we can confirm that the bag is not overfilled

    presents = bagLine.split()
    presentCountSoFar = 0
    bagWtSoFar = 0.0
    for present in presents:
        present = present.strip(" _0123456789") #we should be left with only "blocks", "gloves", "doll", etc.
        if len(present) == 0:
            continue
        presentCountSoFar += 1
        presentWt = genProbWt(present)
        bagWtSoFar += presentWt

    if (presentCountSoFar < 3) or (bagWtSoFar > 50.0):
        bagResults["bagwt"] = 0     #it doesn't matter what we set the bagwt to if the bag is not valid
        bagResults["valid"] = False
    else:
        bagResults["bagwt"] = bagWtSoFar     #it doesn't matter what we set the bagwt to if the bag is not valid
        bagResults["valid"] = True

    return bagLine
#END: def TryEvalBag

def TryEval(submissionText):
    submResults = {}
    submResults["totwt"] = 0
    submResults["numvalidbags"] = 0
    submResults["numinvalidbags"] = 0
    submResults["totwaste"] = 0.0
    submResults["avgwaste"] = 0.0

    bagLines = submissionText.splitlines()

    for bagLine in bagLines:
        bagLine = bagLine.strip()
        if (len(bagLine) == 0) or (bagLine == "Gifts"):
            continue  # skip empty lines and the first line
        bagResults = {}
        bagResults = TryEvalBag(bagLine)
        if bagResults["valid"]:
            submResults["totwt"] += bagResults["bagwt"]
            submResults["numvalidbags"] += 1
            submResults["totwaste"] += 50.0 - bagResults["bagwt"]
        else
            submResults["numinvalidbags"] += 1

    if submResults["numvalidbags"] > 0:
        submResults["avgwaste"] = 0.0
    else:
        submResults["avgwaste"] = float(submResults["totwaste"]) / float(submResults["numvalidbags"])
    return submResults
#END: def TryEval

def TryEvalMultiple(submissionText, multiple):
    submResults = TryEval(submissionText)
    multipleResults = {}
    multipleResults["multipletotwt"] = 0
    multipleResults["multiplenumvalidbags"] = 0
    multipleResults["multiplenuminvalidbags"] = 0
    multipleResults["multipleavgwaste"] = 0.0
    for submIndex in range(multiple):
        submResults = TryEval(submissionText)
        multipleResults["multipletotwt"] += submResults["totwt"]
        multipleResults["multiplenumvalidbags"] += submResults["numvalidbags"]
        multipleResults["multiplenuminvalidbags"] += submResults["numinvalidbags"]
        multipleResults["multipleavgwaste"] += submResults["avgwaste"]
    multipleResults["avgtotwt"] = float(multipleResults["multipletotwt"]) / float(multiple)
    multipleResults["avgnumvalidbags"] = float(multipleResults["multiplenumvalidbags"]) / float(multiple)
    multipleResults["avgnuminvalidbags"] = float(multipleResults["multiplenuminvalidbags"]) / float(multiple)
    multipleResults["avgwaste"] = float(multipleResults["multipleavgwaste"]) / float(multiple)

    return multipleResults
#END: def TryEvalMultiple


#TEST:
print 55.66
submfile = open("..\sample_submission.csv", "r")
submissionText = submfile.read()
multipleResults = TryEvalMultiple(submissionText, 1)
for key in multipleResults:
    print key, multipleResults[key]