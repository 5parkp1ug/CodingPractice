#!/usr/bin/env python3
# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Given a number N. The task is to check whether it is sparse or
#                not. A number is said to be a sparse number if no two or more 
#                consecutive bits are set in the binary representation.
# ==============================================================================

def sparse_number(number: int) -> bool:
    return (number & (number >> 1)) == 0

if __name__ == '__main__':
    print(sparse_number(2))  # Result: True
    print(sparse_number(12))  # Result: False
    print(sparse_number(72))  # Result: True