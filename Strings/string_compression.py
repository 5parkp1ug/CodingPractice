def compress(chars: str) -> int:
    result = []
    last_char = chars[0]
    last_char_count = 1

    for i in range(1, len(chars)):
        if chars[i] != last_char:
            if last_char_count == 1:
                result.extend(last_char)
            else:
                result.append(last_char)
                result.extend([count for count in str(last_char_count)])
            last_char = chars[i]
            last_char_count = 1
        else:
            last_char_count += 1
    result.append(last_char)
    result.extend([count for count in str(last_char_count)])
    
    return len(result)

def compress1(chars: str) -> int:

    pos = 0
    count = 1
    while chars:
        while chars[pos] == chars[i]:
            chars.pop(i)
            count += 1
        pos += 1

    return chars

# print(compress(["a","a","b","b","c","c","c"]))
# print(compress(["a","b","b","c","c","c"]))
print(compress1(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))