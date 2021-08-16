# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Given an array of integers nums and an integer target, return 
#                indices of the two numbers such that they add up to target.
# ==============================================================================

def two_sum(targetSum: int, arr: list) -> None:

	result_map = {}

	for index, num in enumerate(arr):
		if targetSum-num in result_map:
			return [result_map[targetSum-num], index]	
		else:
			result_map[num] = index
	
if __name__ == '__main__':
	# two_sum(7, [5, 3, 4, 7])  # Result: [1, 2]
	print(two_sum(10, [2, 8, 3, 5, 5]))  # Result: [1, 2]
	# print(two_sum(8, [1, 4, 5]))  # Result: [4, 4]
	# print(two_sum(100, [1, 2, 5, 25]))  # Result: [25, 25, 25, 25]