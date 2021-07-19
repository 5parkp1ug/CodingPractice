# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Find leader elements in the aray. An element is called the 
#                leader of an array if there is no element greater than it on 
#                the right side.
# ==============================================================================

def leaders(arr: list) -> None:
    length = len(arr)
    current_leader = arr[length-1]
    print(current_leader)

    for index in range(length-2, -1, -1):
        if current_leader < arr[index]:
            current_leader = arr[index]
            print(current_leader)

if __name__ == '__main__':
    array = [7, 10, 4, 3, 6, 5, 2]  # Result: [10, 6, 5, 2]
    array1 = [1,2,3,4,5,6,7,8,9]  # Result: [9]
    print(f'Leaders of array {array}')
    result = leaders(array)
    print(f'Leaders of array {array1}')
    result1 = leaders(array1)