#!/usr/bin/env python3
# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Find the position of first set bit found from the right side in 
#                the binary representation of the number.
# ==============================================================================

def find_first_set_bit(number: int) -> int:
	if number == 0: return 0

	pos = 1

	while number > 0:
		if (number & 1) == 1:
			return pos
		else:
			number = number >> 1
			pos += 1

if __name__ == '__main__':
	print(find_first_set_bit(18))  # Result: 2
	print(find_first_set_bit(12))  # Result: 3
	print(find_first_set_bit(0))  # Result: 0