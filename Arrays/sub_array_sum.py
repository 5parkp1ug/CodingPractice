def sub_array_sum(arr: list, req_sum: int):
    start = 0
    end = 0
    curr_sum = req_sum
    for i in range(len(arr)):
        curr_sum -= arr[i]
        if curr_sum == 0:
            return (start, end)
        elif curr_sum < 0:
            while curr_sum < 0:
                curr_sum += arr[start]
                start+=1
            end+=1
        else:
            end += 1
        print(f'{start} {end} {curr_sum}')
    return None

print(sub_array_sum([1,4,20,3,10, 5], 33))