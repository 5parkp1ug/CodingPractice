
def reverse_float(n: float) -> float:
	result = ''
	num = str(n)

	q = []

	for i in range(len(num)):
		if num[i] == '.':
			while q:
				result += q.pop()
			result += '.'
		else:
			q.append(num[i])

	while q:
		result += q.pop()

	return float(result)

print(reverse_float(123.89))
print(reverse_float(0.89))