from math import factorial

def ncr(i, n):
    return factorial(n)//(factorial(i)*factorial(n-i))

def combinations(target):
    comblist=[]
    numlist=[]
    def helper(mylist, target, n):
        if len(mylist)==n:
            if sum(mylist)==target:
                comblist.append(mylist)
            return
        for i in range(4):
            helper(mylist+[i], target, n)
    helper(numlist, target, 7)
    return comblist
           
def count(x):
    if not 35<=x<=56:
        return 0
    comblist=combinations(x-35)
##    print(comblist)
    result=0
    for comb in comblist:
        prod=1
        for num in comb:
            prod*=ncr(5+num, 8)
        result+=prod
    return result

if __name__ == "__main__":
##    print(combinations(21))
    print(count(35)) # 1727094849536
    print(count(42)) # 2375030784000
##    print(count(55)) # 56
##    print(count(56)) # 1
##    print(count(80)) # 0
