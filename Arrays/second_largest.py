# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Binary search
# ==============================================================================

def second_largest(arr: list) -> int:
    pos = -1
    largest = -1
    second_largest = -1
    for index, item in enumerate(arr):
        if item > largest:
            second_largest = largest
            largest = item
            pos = index-1
        elif (item < largest) and (item > second_largest):
            second_largest = item
            pos = index

    return pos

if __name__ == '__main__':
    array = [12,7,12,9]
    result = second_largest(array)
    if result != -1: print(f'Second Largest Item found at position {result+1}')
    else: print('Second Largest Item not found')