# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Binary search
# ==============================================================================

def binary_search(arr: list, num: int, left: int = None, right: int = None) -> int:
    if left <= right:
        # calculate mid
        mid = (left + right) // 2
        
        if arr[mid] == num:
            return mid + 1
        
        if num < arr[mid]:
            return binary_search(arr, num, left, mid-1)

        elif num > arr[mid]:
            return binary_search(arr, num, mid+1, right)
    else:
        return -1

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,10]
    result = binary_search(array, 5, 0, len(array)-1)
    if result != -1: print(f'Item found at position {result}')
    else: print('Item not found')