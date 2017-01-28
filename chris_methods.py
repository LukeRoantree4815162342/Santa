
# Note: File designed to help me easily experiment with ideas
# Formatting and general style likely not consistent with most of the other files 

from __future__ import division
import numpy as np
from TryEval import *

# data used
item_names = ["bike","horse","ball","blocks","coal","gloves","train","doll","book"]
initial_item_count = 7166
gift_mass_mean = {	
	"bike":		20.072,
	"horse":	5.0029,
	"ball":		2.0003,
	"blocks":	11.668,
	"coal":		23.472,
	"gloves":	1.4022,
	"train":	10.033,
	"doll":		4.9998,
	"book":		2.0015
}
gift_mass_sd = {	
	"bike":		9.797,
	"horse":	1.988,
	"ball":		0.299,
	"blocks":	3.120,
	"coal":		16.61,
	"gloves":	1.405,
	"train":	4.897,
	"doll":		2.236,
	"book":		2.000
}
gift_count_initial= {
	# initial total = 7166
	"horse":	1000,
	"ball":		1100,
	"bike":		500,
	"train":	1000,
	"coal":		166,
	"book":		1200,
	"doll":		1000,
	"blocks":	1000,
	"gloves":	200	
}

gift_count = {} # number of each item remaining
available_item_names = [] # items of which there are more than zero
available_item_count = initial_item_count # total number of unbagged items

def init():
	# call this everytime a new set of parameters (eg seed, sigmas) is used
	global gift_count
	global available_item_names
	global available_item_count	
	gift_count = gift_count_initial.copy()
	available_item_names = item_names[:]
	available_item_count = initial_item_count
	return

class Bag:
	def __init__(self):
		self.contents = []
		self.mass = 0
		self.sd = 0
		return
	def addItem(self,item):
		self.contents.append(item)
		self.mass+= gift_mass_mean[item]
		self.sd = np.sqrt(self.sd**2+gift_mass_sd[item]**2)
		return
	def removeItem(self,item):
		self.contents.remove(item) # will throw error if item not present.	
		self.mass -= gift_mass_mean[item]
		self.sd = np.sqrt(self.sd**2-gift_mass_sd[item]**2)
		return
	def getRiskFactor(self,sigmas=1):
		# a handy wavey measure of how likely a bag is to rip.
		return self.mass+sigmas*self.sd-50 

def randomFill(maxRisk,sigmas,maxTries = 100000 ):
	# randomly add items until result too risky to add more
	# if unlucky, it will fail.
	global available_item_count
	counter = 0
	while True:
		counter+=1
		if counter>maxTries:
			raise RuntimeError("Unlucky, rerun with different random seed")
		bag = Bag()
		allowedItems = available_item_names[:]
		while len(allowedItems) > 0: 
			# keep adding items until too risky
			newItem = np.random.choice(allowedItems)
			bag.addItem(newItem)
			if bag.getRiskFactor(sigmas) > maxRisk:
				#reject item
				bag.removeItem(newItem)
				allowedItems.remove(newItem)
			else:
				#accept item
				gift_count[newItem] -= 1
				available_item_count -=1
				if gift_count[newItem] < 1:
					available_item_names.remove(newItem)
					allowedItems.remove(newItem)
		if(available_item_count<=0):
			break
		if len(bag.contents) < 3: 
			# reject bag, put items back
			for item in bag.contents:
				if gift_count[item] == 0:
					available_item_names.append(item)
				gift_count[item]+=1
				available_item_count+=1
		else: break
	return bag

def fillBags(mode,maxBags=1000,sigmas=1):
	bags = []
	maxRisk = 0
	if mode == 1: 
	# random fill - no minimum run time, can get stuck in loop
	# will automatically error once loop is discovered
	# inefficient and fairly disgusting but surprisingly effective
		while len(bags) < maxBags:
			bag = randomFill(maxRisk,sigmas)
			bags.append(bag)
		return bags
	else:
		# better methods to come
		raise NotImplementedError("invalid bag fill mode")
	return bags

def writeSubmission(bags,filename):
	#converts array of bags into a submittable file.
	count_items = {
		"horse":	0,
		"ball":		0,
		"bike":		0,
		"train":	0,
		"coal":		0,
		"book":		0,
		"doll":		0,
		"blocks":	0,
		"gloves":	0
	}
	target = open(filename+".csv","w")
	target.write("Gifts\n")
	for bag in bags:
		newline = []
		for item in bag.contents:
			newline.append(item+"_"+str(count_items[item]))
			count_items[item]+=1
		target.write(" ".join(newline))
		target.write("\n")
	#make sure nothing crazy happened:
	for item in count_items:
		if count_items[item] > gift_count_initial[item]:
			raise RuntimeError("Attempted to use too many of item "+item)
	print "Wrote submission as "+filename
	target.close()

# test run

init()
seed = 10
sigmas=1.5
np.random.seed(seed)
try:
	bags = fillBags(1,maxBags=1000,sigmas=sigmas)

	name = "_".join(["chris","seed",str(seed),"sigmas",str(sigmas)])
	writeSubmission(bags,name)
	submfile = open(name+".csv", "r")
	submission_text = submfile.read()
	multiple_results = try_eval_multiple(submission_text, 500)
	print "sigmas,seed",sigmas,seed
	print multiple_results["avgtotwt"]

	# # additional logging
	# exp_mass = 0
	# unused_bags = 0
	# # for bag in bags:
	# # 	exp_mass += bag.mass
	# # 	if len(bag.contents)<3:
	# # 		unused_bags +=1
	# print "maxRisk,sigmas,seed",maxRisk,sigmas,seed
	# print "bags used", len(bags) - unused_bags
	# print "remaining items", available_item_count
	# print "expected mass", exp_mass
	# writeSubmission(bags,"chris1_seed"+str(seed))

	# for key in multiple_results:
	#    print key, multiple_results[key]
except:
	print "bad combo: sigmas,seed:",sigmas,seed
	print "use another seed"