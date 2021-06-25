def can_sum(targetSum, arr, memo = {}):

	if targetSum in memo: return memo[targetSum]

	if targetSum == 0: return True
	if targetSum < 0: return False

	for num in arr:
		remainder = targetSum - num
		if remainder >= 0:
			if can_sum(remainder, arr, memo):
				memo[targetSum] = True
				return True
	
	memo[targetSum] = False
	return False

if __name__ == '__main__':
	print(can_sum(20, [2, 4, 6]))
	print(can_sum(7, [2, 4]))
	print(can_sum(8, [2, 4, 5]))
	print(can_sum(8, [7, 14]))