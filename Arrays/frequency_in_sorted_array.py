# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Find number of times an element occurs in a sorted array.
# ==============================================================================

def frequency(arr: list) -> None:
    length = len(arr)
    index = 1
    count = 1

    while index < length:
        while (index < length) and (arr[index] == arr[index-1]):
            count += 1
            index += 1
        print(arr[index-1], ' - ', count)
        index += 1
        count = 1

if __name__ == '__main__':
    array = [10, 10, 20, 30, 30, 30]
    frequency(array)