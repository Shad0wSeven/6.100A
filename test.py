s = 'abcdefghi'
# count the times of 'a, e i o u' in s

cnt = 0

for i in s:
	if i in 'aeiou':
		cnt += 1

print(cnt)