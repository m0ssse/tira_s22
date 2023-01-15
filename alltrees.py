class AllTrees:
    def __init__(self,n):
        self.edges=[]
        self.n=n

    def repres(self, x, parents):
        while x!=parents[x]:
            x=parents[x]
        return x

    def add_edge(self, a ,b):
        self.edges.append((a, b))

    def istree(self, edges):
        components=self.n
        parents=[i for i in range(self.n+1)]
        compsize=[1]*(self.n+1)
        def repres(x):
            while x!=parents[x]:
                x=parents[x]
            return x

        def merge(a, b):
            a=repres(a)
            b=repres(b)
            if a==b:
                return
            if compsize[a]<compsize[b]:
                a,b=b,a
            parents[b]=a
            compsize[a]+=compsize[b]
        for edge in edges:
            if repres(edge[0])==repres(edge[1]):
                continue
            merge(edge[0], edge[1])
            components-=1
        return components==1
            
            

    def find_edge_combinations(self, edgelist):
        if len(edgelist)==self.n-1:
            self.edgecombs.add(tuple(sorted(edgelist)))
            return
        for edge in self.edges:
            if edge in edgelist:
                continue
            self.find_edge_combinations(edgelist+[edge])
            

    def count(self):
        self.trees=0
        self.edgecombs=set()
        self.find_edge_combinations([])
        for combination in self.edgecombs:
            if self.istree(combination):
                self.trees+=1
        return self.trees
        
        
if __name__ == "__main__":
    a = AllTrees(3)
    a.add_edge(1,2)
    print(a.count()) # 0
    a.add_edge(1,3)
    print(a.count()) # 1
    a.add_edge(2,3)
    print(a.count()) # 3
