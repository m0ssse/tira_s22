def count(s):
    # TODO
##    remcounts={"": 0}
    remcounts={}
    def helper(s, total):
##        print(f"checking {s}")
##        if not s:
##            return 1
        indops=[]
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                indops.append(i)
        if len(indops)==0:
            return 0
        for i in indops:
            newstr=remchars(s, i)
##            print(f"string is now {newstr}")
            if not newstr:
                total+=1
            elif not newstr in remcounts:
                remcounts[newstr]=helper(newstr, 0)
                total+=remcounts[newstr]
            else:
                total+=remcounts[newstr]
        return total
    remcounts[s]=helper(s, 0)
##    print(remcounts)
    return remcounts[s]
    
def remchars(s, i):
    return s[:i]+s[i+2:]

if __name__ == "__main__":
##    mystr="abcdeffghijklmnopqrstuvwxyz"
##    for i in range(len(mystr)-1):
##        print(remchars(mystr, i))
    print(count("1100")) # 2
    print(count("1001")) # 1
    print(count("100111")) # 5
    print(count("11001")) # 0
    print(count("1100110011100111")) # 113925
