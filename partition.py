def check(t):
    total=sum(t)
    subsetlist=subsets(len(t))
    for subset in subsetlist:
        subsetsum=0
        for i in range(len(t)):
            if subset[i]==1:
                subsetsum+=t[i]
        if subsetsum==total-subsetsum:
            return True
    return False

def subsets(n):
    subsetlist=[]
    subset=[]
    def generate(mylist, k):
        if len(mylist)==k:
            subsetlist.append(mylist)
            return
        for i in range(2):
            generate(mylist+[i], k)
    generate(subset, n)
    return subsetlist

if __name__ == "__main__":
    print(check([3,4,5])) # False
    print(check([16,8,4,4])) # True
    print(check([9,4,8,7,6])) # True
    print(check([1,2,3,4,5,6])) # False
    print(check([1,2,3,4,5,6,7])) # True
    print(check([4,4,4,6,6])) # True
