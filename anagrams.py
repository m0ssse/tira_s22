def create(s):
    anagset=set()
    permlist=createperms(len(s))
    for perm in permlist:
        newstr=""
        for i in perm:
            newstr+=s[i-1]
        anagset.add(newstr)
    return sorted(list(anagset))
    
def createperms(n):
    numlist=[]
    permlist=[]
    def helper(nums, n):
        nums=nums[:]
        if len(nums)==n:
            permlist.append(nums)
        else:
            for i in range(1, n+1):
                if i not in nums:
                    new=nums[:]
                    new.append(i)
                    helper(new, n)
    helper(numlist, n)
    return permlist
                    
        
                
        

        

if __name__ == "__main__":
##    createperms(8)
    print(create("ab")) # [ab,ba]
    print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
    print(len(create("aybabtu"))) # 1260
