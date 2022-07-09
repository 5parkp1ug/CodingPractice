def generator(string: str):
    result = []

    for i in range(0, 1<<len(string)):
        temp_string=''
        for j in range(len(string)):
            if (i>>j) & 1 != 0:
                temp_string+=string[j]
        result.append(temp_string)
    return result
    
print(generator('abcd'))