#!/usr/bin/env python3
# ============================================================================
# Created By   : 5parkp1ug
# Description  : Count all possible paths from top left to bottom right of a 
#                mXn matrix
# ============================================================================

def grid_traveller(grid: tuple, memo: dict = None) -> int :
    if memo == None: memo = {} 

    if grid in memo: return memo[grid]

    row, col = grid
    if row == 0 or col == 0:
        return 0

    if row == 1 and col == 1:
        return 1

    no_of_ways = grid_traveller((row-1, col), memo) + grid_traveller((row, col-1), memo)
    memo[grid] = no_of_ways
    return no_of_ways

if __name__ == '__main__':
    print(grid_traveller((18,18)))
