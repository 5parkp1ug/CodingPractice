def reverseWords(s: str) -> str:
    start = None
    end = -1
    result = ''
    
    while end <= len(s)-1:
        while end<=len(s)-1 and s[end] != ' ':
            end += 1
        
        result += s[end-1:start:-1] + ' '
        start = end
        end += 1
    return result.rstrip()

print(reverseWords("the sky is blue"))
# print(reverseWords("hello"))
# print(reverseWords("a good example"))
# print(reverseWords("Alice does not even like bob"))
# print(reverseWords("Bob Loves  Alice "))