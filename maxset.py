class MaxSet:
    def __init__(self,n):
        self.parents=[i for i in range(n+1)]
        self.compsize=[1]*(n+1)
        self.maxsize=1

    def repres(self, x):
        while self.parents[x]!=x:
            x=self.parents[x]
        return x

    def merge(self,a,b):
        a=self.repres(a)
        b=self.repres(b)
        if a==b:
            return
        if self.compsize[a]<self.compsize[b]:
            a,b=b,a
        self.parents[b]=a
        self.compsize[a]+=self.compsize[b]
        self.maxsize=max(self.maxsize, self.compsize[a])
        

    def get_max(self):
        return self.maxsize

if __name__ == "__main__":
    m = MaxSet(5)
    print(m.get_max()) # 1
    m.merge(1,2)
    m.merge(3,4)
    m.merge(3,5)
    print(m.get_max()) # 3
    m.merge(1,5)
    print(m.get_max()) # 5
