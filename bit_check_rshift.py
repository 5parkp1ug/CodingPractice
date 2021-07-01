#!/usr/bin/env python3
# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Check if the k'th bit is set for a number n using right-shift
# 				 operator
# ==============================================================================

def bit_check_lshift(number: int, position: int) -> bool:
    return ((number >> (position - 1)) & 1) == 1

if __name__ == '__main__':
    print(bit_check_lshift(5, 1)) # Result: True
    print(bit_check_lshift(8, 2)) # Result: False
    print(bit_check_lshift(0, 3)) # Result: False
    print(bit_check_lshift(5, 3)) # Result: True