def count_sqrts(nums_list):
	assert len(nums_list) > 0, "nums_list is empty"
	for num in nums_list:
		if num < 0:
			raise ValueError("nums_list contains negative numbers")
		if nums_list.count(num) > 1:
			raise ValueError("nums_list contains duplicates")
	count = 0
	for num in nums_list:
		if num**2 in nums_list:
			count += 1
	return count
