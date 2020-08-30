def lcs(a,b):

	if len(a) == 0 or len(b) == 0:
		return(0)

	L = [[0 for i in range(len(a)+1)] for j in range(len(b)+1)]
	# print(L)
	for i in range(1, len(b)+1):
		for j in range(1, len(a)+1):
			if a[j-1] == b[i-1]: 
				L[i][j] = L[i-1][j-1] + 1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])
	print(L[len(b)][len(a)])
	return(L)

def find_sequence(result, a, b):
	sequence = []
	i = len(result)-1
	j = len(result[i])-1

	while i-1 > 0 or j-1 > 0:
		# print(sequence)
		if result[i][j] == result[i-1][j]:
			i -= 1
		elif result[i][j] == result[i][j-1]:
			j -= 1
		else:
			sequence.append(a[j-1])
			i -= 1
			j -= 1
	print(sequence[::-1])

a = 'FURQAAN'
b = 'UANW'


result = lcs(a,b)
for i in result:
	print(i)
find_sequence(result, a, b)