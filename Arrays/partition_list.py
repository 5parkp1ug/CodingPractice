def partition_list(arr: list[int], val: int) -> list[int]:
	before = []
	after = []
	print(f'arr={arr}')
	for index, num in enumerate(arr):
		if num <= val:
			print(f'num={num} less than val')
			before.append(num)
		else:
			print(f'num={num} greater than val')
			after.append(num)
	
	print(f'before={before} after={after}')
	return before+after


if __name__ == '__main__':
	print(partition_list([1,4,3,2,7, 5,2], 3))