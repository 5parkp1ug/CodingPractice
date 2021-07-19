# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Left Rotate a given item by k position
# ==============================================================================

def left_rotate(arr: list, k: int) -> list:
    count = 0
    temp = []
    rotation_count = k % len(arr)
    while count <= rotation_count-1:
        temp.append(arr.pop(0))
        count += 1
    result =  arr + temp
    return result

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9,10]
    result = left_rotate(array, 11)
    print(f'Result - {result}')
