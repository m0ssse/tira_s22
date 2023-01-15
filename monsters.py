def count(r):
    n=len(r)
    countmat=[[0 for i in range(n)] for j in range(n)]
    if r[0][0]=="@":
        countmat[0][0]=1
    if r[0][0]=="#":
        return -1
##    for row in r:
##        print(row)
##    print(0, 0)
##    for row in countmat:
##        print(row)
##    print()
    for i in range(1,n): #first column
##        print(i, 0)
        if r[i][0]=="@":
            countmat[i][0]=countmat[i-1][0]+1
        elif r[i][0]=="#":
            countmat[i][0]=len(r)**2
        else:
            countmat[i][0]=countmat[i-1][0]
##        for row in countmat:
##            print(row)
##        print()
    for j in range(1, n): #first row
##        print(0, j)
        if r[0][j]=="@":
            countmat[0][j]=countmat[0][j-1]+1
        elif r[0][j]=="#":
            countmat[0][j]=n**2
        else:
            countmat[0][j]=countmat[0][j-1]
##        for row in countmat:
##            print(row)
##        print()
    for i in range(1, n):
        for j in range(1, n):
##            print(i, j)
            if r[i][j]=="@":
                countmat[i][j]=min(countmat[i-1][j], countmat[i][j-1])+1
            elif r[i][j]=="#":
                countmat[i][j]=n**2
            else:
                countmat[i][j]=min(countmat[i-1][j], countmat[i][j-1])
##            for row in countmat:
##                print(row)
##            print()
##    for row in countmat:
##        print(row)
    if countmat[n-1][n-1]>=n**2:
        return -1
    return countmat[n-1][n-1]
                
if __name__ == "__main__":
    r = ["....@",
         "@##.#",
         ".##@#",
         ".@..#",
         "###@."]
    print(count(r)) # 2

    r=["#@.@#",
       "@...@",
       "@@@##",
       "@#@@@",
       "@.#@@"]
    print(count(r)) # 2
