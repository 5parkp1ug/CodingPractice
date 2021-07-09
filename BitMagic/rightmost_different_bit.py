#!/usr/bin/env python3
# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Given two numbers M and N. The task is to find the position of 
#                the rightmost different bit in the binary representation of 
#                numbers.
# ==============================================================================

def rightmost_different_bit(m: int, n: int) -> int:
	count = 1
	
	while (m > 0) or (n > 0):
		if (m&1) == (n&1): 
			count+=1
		else:
			break
		m = m>>1
		n = n>>1
		
	return count

if __name__ == "__main__":
	print(rightmost_different_bit(11, 9))  # Result: 2
	print(rightmost_different_bit(52, 4))  # Result: 5