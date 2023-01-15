class Components:
    def __init__(self,n):
        self.n=n
        self.edges=[]
        self.parents=[i for i in range(self.n+1)]
        self.compsize=[1 for _ in range(self.n+1)]
        self.components=n
        
    def repres(self, x):
        while x!=self.parents[x]:
            x=self.parents[x]
        return x

    def same(self, a, b):
        return self.repres(a)==self.repres(b)

    def merge(self, a, b):
        if self.same(a,b):
            return
        a=self.repres(a)
        b=self.repres(b)
        if self.compsize[a]<self.compsize[b]:
            a, b=b, a
        self.parents[b]=a
        self.compsize[a]+=self.compsize[b]
        self.components-=1

    def add_road(self,a,b):
        self.merge(a, b)

    

    def count(self):
        return self.components

if __name__ == "__main__":
    c = Components(5)
    print(c.count()) # 5
    c.add_road(1,2)
    c.add_road(1,3)
    print(c.count()) # 3
    c.add_road(2,3)
    print(c.count()) # 3
    c.add_road(4,5)
    print(c.count()) # 2
