def find(t):
    k=[1]
    for i in range(1, len(t)):
        longest=0
        for j in range(i-1, -1, -1):
            if -1<=t[j]-t[i]<=1:
                longest=max(longest, k[j])
        k.append(longest+1)
    return max(k)
if __name__ == "__main__":
    print(find([1,2,3,4,5])) # 5
    print(find([5,5,5,5,5])) # 5
    print(find([5,2,3,8,2,4,1])) # 4
    print(find([1,3,5,7,9])) # 1
