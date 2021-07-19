# ==============================================================================
# Created By   : 5parkp1ug
# Description  : For a given array move the zeros to the end preserving the 
#                order of other elements.
# ==============================================================================
import time


def move_zeros1(arr: list) -> list:
    '''
    Naive method with time complexity - O(n^2)
    '''
    length = len(arr)

    for index in range(length):
        if arr[index] == 0:
            for i in range(index+1, length):
                if arr[i] != 0:
                    arr[index], arr[i] = arr[i], arr[index]
                    break
    return arr

def move_zeros2(arr:list) -> list:
    '''
    Efficient method with time complexity - O(n)
    '''
    count = 0
    
    for index, item in enumerate(arr):
        if item != 0:
            arr[count], arr[index] = arr[index], arr[count]
            count += 1
    
    return arr



if __name__ == '__main__':
    array = [12,0,12,9, 0, 5, 7]
    tic = time.perf_counter_ns()
    result1 = move_zeros1(array)
    toc = time.perf_counter_ns()
    print(f'Result 1 - {result1} \n Time elapsed - {toc-tic:0.2f} ns')

    tic = time.perf_counter_ns()
    result2 = move_zeros2(array)
    toc = time.perf_counter_ns()
    print(f'Result 2 - {result2} \n Time elapsed - {toc-tic:0.2f} ns')