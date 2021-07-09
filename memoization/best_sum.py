#!/usr/bin/env python3
# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Given an array arr[] of integers and an integer K, 
#                the task is to print smallest subset of the given array with 
#                the sum equal to the given target K.
# ==============================================================================

def best_sum(targetSum: int, arr: list, memo={}) -> list:

	if targetSum in memo: return memo[targetSum]

	if targetSum == 0: return []
	if targetSum < 0: return None

	shortest_combination = None

	for num in arr:
		remainder = targetSum - num
		remainder_combination = best_sum(remainder, arr, memo)
		if remainder_combination is not None:
			combination = [*remainder_combination, num]
			if shortest_combination is None or len(shortest_combination) > len(combination):
				shortest_combination = combination
	
	memo[targetSum] = shortest_combination
	return shortest_combination

if __name__ == '__main__':
	print(best_sum(7, [5, 3, 4, 7]))  # Result: [7]
	print(best_sum(8, [2, 3, 5]))  # Result: [3, 5]
	print(best_sum(8, [1, 4, 5]))  # Result: [4, 4]
	print(best_sum(100, [1, 2, 5, 25]))  # Result: [25, 25, 25, 25]