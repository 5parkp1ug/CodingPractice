#!/usr/bin/env python3
# ==================================================================================
# Created By   : 5parkp1ug
# Description  : Given a set of non-negative integers, and a value sum, determine
#                if there is a subset of the given set with sum equal to given sum. 
# ==================================================================================

def can_sum(targetSum: int, arr: list, memo = None) -> bool:
	if memo == None: memo = {}

	if targetSum in memo: return memo[targetSum]

	if targetSum == 0: return True
	if targetSum < 0: return False

	for num in arr:
		remainder = targetSum - num
		if can_sum(remainder, arr, memo):
			memo[targetSum] = True
			return True
	
	memo[targetSum] = False
	return False

if __name__ == '__main__':
	print(can_sum(20, [2, 4, 6]))  # Result: True
	print(can_sum(7, [2, 4]))  # Result: False
	print(can_sum(8, [2, 4, 5]))  # Result: True
	print(can_sum(300, [7, 14]))  # Result: False