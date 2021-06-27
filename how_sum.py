def how_sum(targetSum: int, arr: list, memo=None) -> list:

	if memo == None: memo = {}

	if targetSum == 0: return []
	if targetSum in memo: return memo[targetSum]
	# if targetSum < 0: return None

	for num in arr:
		remainder = targetSum - num
		if remainder >= 0:
			remainder_result = how_sum(remainder, arr, memo)

			if remainder_result is not None:
				memo[targetSum] = [*remainder_result, num]
				return memo[targetSum]

	memo[targetSum] = None
	return memo[targetSum]

if __name__ == '__main__':
	print(how_sum(7, [2, 3]))
	print(how_sum(7, [5, 3, 4, 7]))
	print(how_sum(300, [7, 14]))