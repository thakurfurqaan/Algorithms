import time

l = 1000000000

a = [i for i in range(l)]
b = [i for i in range(l)]

# list that stores the same values as a and b
c = [[i,i] for i in range(l)] 

# traversing through 2 different lists
start = time.time()
d = []
for i in range(l):
	for j in range(l):
		d.append(str(a[i]) + " " + str(b[j]))
print("Traversing through a and b: " + str(time.time() - start))

# traversing through the sublists of a list
start = time.time()
d = []
for i in range(l):
	for j in range(l):
		d.append(str(c[i]) + " " + str(c[j]))
print("Traversing through sublists of c: " + str(time.time() - start))