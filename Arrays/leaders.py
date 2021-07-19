# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Find leader elements in the aray. An element is called the 
#                leader of an array if there is no element greater than it on 
#                the right side.
# ==============================================================================

def leaders(arr: list) -> list:
    length = len(arr)
    temp = []
    for index, item in enumerate(arr):
        if index == length-1:
            temp.append(item)
        elif item > arr[index+1]:
            temp.append(item)
    return temp

if __name__ == '__main__':
    array = [7, 10, 4, 3, 6, 5, 2]  # Result: [10, 4, 6, 5, 2]
    array1 = [1,2,3,4,5,6,7,8,9]  # Result: [9]
    result = leaders(array)
    result1 = leaders(array1)
    print(f'The leaders of given array are - {result}')
    print(f'The leaders of given array are - {result1}')