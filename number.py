def count(n):
    total=[]   
    def helper(numtoadd, totalsofar, target):
        rem=target-totalsofar
##        print(f"{rem} remaining")
        if target==totalsofar:
##            print("match")
            total.append(1)
            return
        if rem<numtoadd:
##            print("overshoot")
            return
        howmany=rem//numtoadd
##        print(f"adding up to {howmany} {numtoadd}s")
        for i in range(howmany+1):
            helper(numtoadd+1, totalsofar+i*numtoadd, target)

    helper(1, 0, n)
    return len(total)

if __name__ == "__main__":
    print(count(4)) # 5
    print(count(5)) # 7
    print(count(8)) # 22
    print(count(42)) # 53174
