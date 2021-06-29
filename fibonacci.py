#!/usr/bin/env python3
# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Fibonacci series via memoization
# ============================================================================
def fibonacci(count, memo={}):
	if count in memo: return memo[count]

	if count == 0: return 0 
	if count == 1: return 1

	sum =  fibonacci(count - 1) + fibonacci(count - 2)
	memo[count] = sum
	return sum

if __name__ == "__main__":
    print(fibonacci(40))