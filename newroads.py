class NewRoads:
    def __init__(self,n):
        self.n=n
        self.roads=[]

    
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

    def add_road(self,a,b,x):
        self.roads.append((x, a, b))

    def min_cost(self):
        self.parents=[i for i in range(self.n+1)]
        self.compsize=[1]*(self.n+1)
        self.cost=0
        self.roads=sorted(self.roads)
        self.components=self.n
        for road in self.roads:
            if self.same(road[1], road[2]):
                continue
            self.merge(road[1], road[2])
            self.cost+=road[0]
        if self.components==1:
            return self.cost
        return -1

if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1,2,2)
    n.add_road(1,3,5)
    print(n.min_cost()) # -1
    n.add_road(3,4,4)
    print(n.min_cost()) # 11
    n.add_road(2,3,1)
    print(n.min_cost()) # 7
