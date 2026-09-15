# Iterative binary search (Given Implementation)#

def binary_search(a_list, item):
	first = 0
	last = len(a_list) - 1
	found = False

	while first <= last and not(found):
		mid = (first + last)//2
		if a_list[mid] == item:
			found = True
		else:
			if item < a_list[mid]:
				last = mid - 1	# search in the first half
			else:
				first = mid + 1	# search in the second half

	if found:
		return mid
	else:
		return -1

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 31))