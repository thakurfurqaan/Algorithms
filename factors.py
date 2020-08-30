import time
import math

def solve(n):
	factors = list()

	for i in range(1, int(math.sqrt(n))+1):
		if n%i == 0:
			factors.append(i)
			if n//i not in factors:
				factors.append(n//i)
	return(sorted(factors))


# n = int(input())
# n = 99999999999999
n = 225
# n = 99999999
start = time.time()
print(solve(n))
print(str(time.time()-start))