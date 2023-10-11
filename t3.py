def get_min(d):
	index = 1000
	value = None
	for key in d:
		if ord(key) < index:
			index = ord(key)
			value = d[key]

	return value

def custom_repeat(L, x):
	for i in range(len(L)): # iterates through every value,
		for j in range(x-1): # append a new value counter times
			L.append(L[i])
	L.sort() # sort the list into ascending order at the end

