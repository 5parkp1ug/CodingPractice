# ==============================================================================
# Created By   : 5parkp1ug
# Description  : Given a list of numbers, return an array with product of numbers
#                except itself. Ex - [1, 2, 3, 4, 5] --> [120, 60, 40, 30, 24]
# ==============================================================================

def product(array: list) -> None:
    length = len(array)
    left_prod = [0]*length
    right_prod = [0]*length
    final_array = []

    left_prod[0] = 1
    right_prod[length-1] = 1

    for i in range(1, length):
        left_prod[i] = left_prod[i-1] * array[i-1]
    
    for j in range(length-2, -1, -1):
        right_prod[j] = right_prod[j+1] * array[j+1]
    
    for i in range(length):
        final_array.append(left_prod[i]*right_prod[i])
    
    print(final_array)

if __name__ == '__main__':
    product([1, 2, 3, 4, 5])