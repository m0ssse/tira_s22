def count(t):
    maxsum=sum(t)
    helper=[[0 for i in range(maxsum+1)] for j in range(len(t)+1)]
    sumsofar=0
    for i in range(len(t)+1):
        helper[i][0]=1
    for i in range(1, len(t)+1):
##        print(sumsofar)
        for j in range(sumsofar+1):
            if helper[i-1][j]:
                helper[i][j]=1
##            if helper[i][j]:
                helper[i][j+t[i-1]]=1
        sumsofar+=t[i-1]        
##    [print(row) for row in helper]
    return sum(helper[-1])-1

if __name__ == "__main__":
    print(count([3,4,5])) # 7
    print(count([1,1,2])) # 4
    print(count([2,2,2,3,3,3])) # 13
    print(count([42,5,5,100,1,3,3,7])) # 91
