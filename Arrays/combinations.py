from collections import *
def combinations(n,k):
    res = []
    
    def generate(n,k,start, temp):
        if len(temp) == k:
            res.append(temp[::])
        
        for i in range(start, n+1):
            temp.append(i)
            generate(n,k,i+1,temp)
            temp.pop()
    
    generate(n,k,1,[])

    return res

if __name__ == '__main__':
    print(combinations(4,2))