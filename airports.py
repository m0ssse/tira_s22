class Airports:
    def __init__(self,n):
        self.graph=[[] for _ in range(n+1)]
        self.graph_rev=[[] for _ in range(n+1)]
        self.n=n

    def add_link(self,a,b):
        self.graph[a].append(b)
        self.graph_rev[b].append(a)

    def dfs(self, x, graph):
        if self.visited[x]:
            return
        self.visited[x]=True
        for neighb in graph[x]:
            self.dfs(neighb, graph)
        self.order.append(x)
        

    def check(self):
        self.order=[]
        self.visited=[False]*(self.n+1)
        for i in range(1, self.n+1):
            self.dfs(i, self.graph)
        self.visited=[False]*(self.n+1)
        components=0
        self.reverse=self.order[::-1]
        self.order.clear()
##        print(self.reverse)
        for i in range(self.n):
            if not self.visited[self.reverse[i]]:
                components+=1
                self.dfs(self.reverse[i], self.graph_rev)
        return components==1
            

if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1,2)
    a.add_link(2,3)
    a.add_link(1,3)
    a.add_link(4,5)
    print(a.check()) # False
    a.add_link(3,5)
    a.add_link(1,4)
    print(a.check()) # False
    a.add_link(5,1)
    print(a.check()) # True
