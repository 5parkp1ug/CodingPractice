#!/usr/bin/env python3
# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Given an array arr[] of integers and an integer K, 
#                the task is to print smallest subset of the given array with
# 				 the sum equal to the given target K using TABULATION.
# ==============================================================================

def best_sum(targetSum: int, arr: list) -> list:
	table = [None] * (targetSum + 1)
	table[0] = []

	for count in range(targetSum + 1):
		if table[count] is not None:
			for num in arr:
				if count+num <= targetSum: 
					combination = [*table[count], num]
					if table[count + num] is None or (len(table[count + num]) > len(combination)):
						table[count + num] = combination
	
	return table[targetSum]

if __name__ == '__main__':
	print(best_sum(7, [5, 3, 4, 7]))  # Result: [7]
	print(best_sum(8, [2, 3, 5]))  # Result: [3, 5]
	print(best_sum(8, [1, 4, 5]))  # Result: [4, 4]
	print(best_sum(100, [1, 2, 5, 25]))  # Result: [25, 25, 25, 25]