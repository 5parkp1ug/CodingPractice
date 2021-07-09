#!/usr/bin/env python3
# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Count number of set bits for a given number n
# ==============================================================================

def count_set_bit(number: int) -> int:
    count = 0
    while number != 0:
        count += (number & 1)
        number = number >> 1
    return count

if __name__ == '__main__':
    print(count_set_bit(3))  # Result: 2
    print(count_set_bit(5))  # Result: 2
    print(count_set_bit(13))  # Result: 3
    print(count_set_bit(28))  # Result: 3
    print(count_set_bit(32))  # Result: 1