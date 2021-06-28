#!/usr/bin/env python3
# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Calculating the nth Fibonacci number using tabulation technique
# ==============================================================================

def fib(n: int) -> int:
	arr = [0] * (n+1)
	arr[1] = 1
	for index in range(n-1):
		arr[index+1] += arr[index]
		arr[index+2] += arr[index]
	arr[-1] += arr[-2]
	
	return arr[-1]

if __name__ == '__main__':
	print(fib(6))
	print(fib(7))
	print(fib(8))
	print(fib(50))