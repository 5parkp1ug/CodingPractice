#!/usr/bin/env python3
# ==================================================================================
# Created By   : 5parkp1ug
# Description  : Given a set of non-negative integers, and a value sum, determine
#                if there is a subset of the given set with sum equal to given sum
#                using TABULATION. 
# ==================================================================================

def can_sum(targetSum: int, arr: list) -> bool:
	table = [False] * (targetSum+1)
	table[0] = True
	
	for count in range(targetSum+1):
		if table[count]:
			for num in arr:
				if count+num <= targetSum: table[count+num] = True

	return table[targetSum]

if __name__ == '__main__':
	print(can_sum(7, [2, 3]))  # Result: True
	print(can_sum(7, [5, 3, 4, 7]))  # Result: True 
	print(can_sum(7, [2, 4]))  # Result: False
	print(can_sum(8, [2, 3, 5]))  # Result: True
	print(can_sum(300, [7, 14]))  # Result: False