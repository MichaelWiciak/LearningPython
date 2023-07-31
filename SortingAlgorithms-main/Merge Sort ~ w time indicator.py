import time, random

def merge_sort(m):
	if len(m) <= 1:
		return m
 
	middle = len(m) // 2
	left = m[:middle]
	right = m[middle:]
 
	left = merge_sort(left)
	right = merge_sort(right)
	return list(merge(left, right))

def merge(left, right):
	result = []
	left_idx, right_idx = 0, 0
	while left_idx < len(left) and right_idx < len(right):
		if left[left_idx] <= right[right_idx]:
			result.append(left[left_idx])
			left_idx += 1
		else:
			result.append(right[right_idx])
			right_idx += 1
	if right_idx == len(right):
		result.extend(left[left_idx:])
	else:
		result.extend(right[right_idx:])
	return result

someList = []
for i in range(1000):
	someList.append(random.randint(1,100)+i)
print(someList)
start = time.time()
someList = merge_sort(someList)
end = time.time()
print(end - start, 'seconds')
print(someList)
