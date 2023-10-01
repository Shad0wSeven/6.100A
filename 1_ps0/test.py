def dot_product(tA, tB):
	"""
	tA: a tuple of numbers
	tB: a tuple of numbers of the same length as tA
	Returns a tuple where the:
	* first element is the length of one of the tuples
	* second element is the sum of the pairwise products of tA and tB
	"""
	# Your code here
	return (len(tA), sum([tA[i]*tB[i] for i in range(len(tA))]))