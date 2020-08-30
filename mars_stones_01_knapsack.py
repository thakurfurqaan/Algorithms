'''
Problem Statement: Find the maximum number of stones which are not common
to Earth and Mars and that can be put inside the Bag with capacity of BagCapacity.

nCommonStones are the number of Common Stones for Earth and Mars and CommonStones 
are the weights of those common stones. 

There are BagCapacity number of stones of weights 1, 2, ..., BagCapacity avaulable.
'''

def solve(BagCapacity, nCommonStones, CommonStones):

	if BagCapacity == 0 or BagCapacity-nCommonStones == 0: return(0)
	if BagCapacity == 1: return(1)

	arr = [x for x in range(1, BagCapacity+1) if x not in CommonStones]
	s, l = 0, 0

	for i in arr:
		if s <= BagCapacity:
			l += 1
			s += 1
	return(l-1)

BagCapacity = 10
nCommonStones = 3
CommonStones = [1,3,5]

result = solve(BagCapacity, nCommonStones, CommonStones)
print("Maximum unique stones that can be collected: " + str(result))