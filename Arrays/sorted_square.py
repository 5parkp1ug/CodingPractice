def sortedSquares(nums: list) -> list:
	result = []
	right = 0
	
	if len(nums) == 1: return [nums[0]*nums[0]]

	while right < len(nums) and nums[right] < 0:
		right += 1
		print(right)
	left = right - 1

	while right < len(nums) and left >= 0:
		if nums[left]* nums[left] < nums[right] * nums[right]:
			result.append(nums[left]* nums[left])
			left -= 1
		elif nums[left]* nums[left] >= nums[right] * nums[right]:
			result.append(nums[right] * nums[right])
			right += 1
	print(f'left={left} right={right}')

	if left != -1:
		while left > -1:
			result.append(nums[left]* nums[left])
			left -= 1

	if right < len(nums):
		while right < len(nums):
			result.append(nums[right] * nums[right])
			right += 1

	return result

print(sortedSquares([-10000,-9999,-7,-5,0,0,10000]))