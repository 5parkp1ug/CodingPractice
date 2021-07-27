# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Water trapping problem.
# ==============================================================================

def water_trapping(arr: list) -> None:
    length = len(arr)
    lmax = [0] * length
    rmax = [0] * length
    lmax[0] = arr[0]
    
    for index in range(1, length):
        lmax[index] = max(arr[index], lmax[index-1])
    
    rmax[length-1] = arr[length-1]
    for rindex in range(length-2, -1, -1):
        rmax[rindex] = max(arr[rindex], rmax[rindex+1])

    print(lmax)
    print(rmax)
    result = 0 

    for i in range(1, length-1):
        result += (min(lmax[i], rmax[i]) - arr[i])

    print(result)

if __name__ == '__main__':
    # array = [5, 0, 6, 2, 3]
    # array = [3, 0, 1, 2, 5]
    # array = [3, 0, 2, 0, 4]
    array = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    water_trapping(array)