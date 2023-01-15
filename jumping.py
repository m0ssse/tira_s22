def count(n,a,b):
    counts=[0]*(n+1)
    counts[b]=1
    for i in range(0, b, a):
        counts[i]+=1
    if b%a==0:
        counts[b]+=1
    for i in range(b, n+1):
        counts[i]=counts[i-b]+counts[i-a]
    return counts[-1]
    
        

if __name__ == "__main__":
    print(count(4,1,2)) # 5
    print(count(10,2,5)) # 2
    print(count(10,6,7)) # 0
    print(count(30,3,5)) # 58
    print(count(50,2,3)) # 525456
