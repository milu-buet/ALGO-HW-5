#!/usr/bin/env python

#print('hello')

#votes = [ 'c', 't', 's', 'j', 'c', 'c', 't', 'c', 't', 'c','c' ]
#votes2 = [2, 1, 1, 0, 2, 1, 2, 1, 2, 1, 0, 2, 1, 2, 1, 0, 0, 2, 1, 0, 0, 2, 0, 2, 0, 1, 1, 2, 1, 1, 2, 1, 1, 0, 2, 1, 2, 1, 0, 2, 0, 1, 2, 2, 2, 0, 0, 1, 0, 2, 2, 2, 0, 2, 0, 0, 2, 2, 1, 2, 1, 0, 2, 0, 2, 0, 0, 0, 0, 2, 2, 0, 0, 0, 1, 1, 2, 2, 2, 2, 0, 1, 1, 0, 0, 1, 2, 2, 0, 2, 2, 2, 2, 1, 2, 0, 0, 1, 0, 1]
# an element is a majority if it occurs more than half of the time.

def brute_force(L):
	for x in L:
		count = 0
		for y in L:
			if x == y:
				count += 1
		#print(count)
		if count > len(L)/2:
			return x
	return None


def pair_up(L,NL):
	if len(NL) == 0:
		return None
	elif len(NL) == 1:   # only one majority cadidate
		count0 = 0
		for i in range(len(L)):
			if L[i] == NL[0]:
				count0+=1
		if count0 > len(L)/2:
			return NL[0]
		return None

	elif len(NL) == 2 and NL[0] != NL[1]: # there is two cadidates to be majority
		count0 = 0
		count1 = 0
		for i in range(len(L)):
			if L[i] == NL[0]:
				count0+=1
			if L[i] == NL[1]:
				count1+=1

		if count0 > len(L)/2:
			return NL[0]
		if count1 > len(L)/2:
			return NL[1]
		return None

	new_L = []
	for i in range(len(NL)-1):   #pair up (0,1)(2,3)(4,5) ...etc and eliminate different
		if i%2 == 0 and NL[i] == NL[i+1]:  #starting of a pair is always even index
			new_L.append(NL[i])
	
	if len(NL) % 2 == 1:
		new_L.append(NL[len(NL)-1])

	#print(new_L)

	return pair_up(L,new_L)

def majority_pair_up(L):
	return pair_up(L,L)


# print(votes)
# a = majority_pair_up(votes)
# b = brute_force(votes)

# print(a,b)

import util
import time
for m in range(100):
	votes = util.random_list(100, 0, 2)
	start1 = time.time()
	a = brute_force(votes)
	end1 = time.time()

	start2 = time.time()
	b = majority_pair_up(votes)
	end2 = time.time()

	#print(votes)
	print("brute-force:ans=%s,time=%s  pair-up:ans=%s,time=%s"%(a,end1-start1,b,end2-start2))

	if a!= b:
		print('Answers dont match!')