#!/usr/bin/env python3
# ============================================================================
# Created By   : 5parkp1ug
# Description  : Count all possible paths from top left to bottom right of a 
#                mXn matrix using TABULATION
# ============================================================================

def grid_traveller(grid: tuple) -> int :
    row, col = grid
    arr = [[0]*(col+1) for i in range(row+2)]
    arr[1][1] = 1
    for r in range(row+1):
        for c in range(col+1):
            current_item = arr[r][c]
            if c+1<=col: arr[r][c+1] += current_item
            if r+1<=row: arr[r+1][c] += current_item
    return arr[row][col]

if __name__ == '__main__':
    print(grid_traveller((1,1)))  # Result: 1
    print(grid_traveller((2,3)))  # Result: 3
    print(grid_traveller((3,2)))  # Result: 3
    print(grid_traveller((3,3)))  # Result: 6
    print(grid_traveller((18,18)))  # Result: 2333606220
