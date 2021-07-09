#!/usr/bin/env python3
# ==================================================================================
# Created By   : 5parkp1ug
# Description  : Given a set of non-negative integers, and a value sum, determine
#                the smallest subset of the given set with sum equal to given sum
#                using TABULATION. 
# ==================================================================================

def how_sum(targetSum: int, arr: list) -> list:
	table = [None] * (targetSum + 1)
	table[0] = []

	for count in range(targetSum + 1):
		if table[count] is not None:
			for num in arr:
				if count+num <= targetSum: table[count + num] = [*table[count], num]
	return table[targetSum]

if __name__ == '__main__':
	print(how_sum(7, [2, 3]))  # Result: [3, 2, 2]
	print(how_sum(7, [5, 3, 4, 7]))  # Result: [4, 3]
	print(how_sum(300, [7, 14]))  # Result: None