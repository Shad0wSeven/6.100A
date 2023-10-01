def flatten(L):
	"""
	L: a list
	Returns a copy of L, which is a flattened version of L
	"""
	if L == []:
		return L
	if isinstance(L[0], list):
		return flatten(L[0]) + flatten(L[1:])
	return L[:1] + flatten(L[1:])