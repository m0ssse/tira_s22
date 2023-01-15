class Cycles:
    def __init__(self,n):
        self.n=n
        self.graph=[[] for _ in range(n+1)]

    def add_edge(self,a,b):
        self.graph[a].append(b)

    def check(self):
        colors=[0]*(self.n+1)
        cycle=[False]
        def helper(vertex):
##            print(f"checking vertex {vertex}")
            if cycle[0]:
                return
            if colors[vertex]==2:
                return
            if colors[vertex]==1:
                cycle[0]=True
                return
            colors[vertex]=1
            for neighb in self.graph[vertex]:
                helper(neighb)
            colors[vertex]=2
        for i in range(1, self.n+1):
            if colors[i]==0:
                helper(i)
        return cycle[0]
        

if __name__ == "__main__":
    c = Cycles(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(1,3)
    c.add_edge(3,4)
    print(c.check()) # False
    c.add_edge(4,2)
    print(c.check()) # True
