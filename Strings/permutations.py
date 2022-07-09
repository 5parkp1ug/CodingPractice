def permutations(prefix, s):
    if len(s) == 1:
        print(s+prefix)
    
    for i in range(0, len(s)):
        permutations(prefix+s[i], s[0:i]+s[i+1:len(s)])

if __name__ == '__main__':
    permutations('','abc')