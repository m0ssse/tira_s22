class SameWeight:
    def __init__(self,n):
        self.edges=[]
        self.n=n

    def add_edge(self,a,b,x):
        self.edges.append((x, a, b))

    def repres(self, x, parents):
##        print("checking repres")
        while parents[x]!=x:
##            print(x)
            x=parents[x]
        return x

    def merge(self, a, b, parents, compsizes):
        a=self.repres(a, parents)
        b=self.repres(b, parents)
        if a==b:
            return
        if compsizes[a]<compsizes[b]:
            a,b=b,a
        parents[b]=a
        compsizes[a]+=compsizes[b]
        

    def check(self):
        self.edges.sort()
        self.parents_min=[i for i in range(self.n+1)]
        self.parents_max=self.parents_min[:]
        self.compsize_min=[1]*(self.n+1)
        self.compsize_max=self.compsize_min[:]
        self.components=self.n
        minweight=0
        maxweight=0
        for i in range(len(self.edges)):
            minedge=self.edges[i]
            maxedge=self.edges[-(i+1)]
            if self.repres(minedge[1], self.parents_min)!=self.repres(minedge[2], self.parents_min):
                self.merge(minedge[1], minedge[2], self.parents_min, self.compsize_min)
                minweight+=minedge[0]
                self.components-=1
            if self.repres(maxedge[1], self.parents_max)!=self.repres(maxedge[2], self.parents_max):
                self.merge(maxedge[1], maxedge[2], self.parents_max, self.compsize_max)
                maxweight+=maxedge[0]
        return minweight==maxweight or self.components>1

            
        

if __name__ == "__main__":
    s = SameWeight(5)
    s.add_edge(2,5,1)
    s.add_edge(3,4,10)
    s.add_edge(4,5,9)
    s.add_edge(3,5,5)
    print(s.check())
    print(s.check())
    s.add_edge(2,4,1)
    print(s.check())
    print(s.check())
