class GraphGame:
    def __init__(self,n):
        self.graph=[[] for _ in range(n+1)]

    def add_link(self,a,b):
        self.graph[a].append(b)

    def winning(self,x):
        restable={}

        def helper(vertex):
            reslist=[True]
            for neighb in self.graph[vertex]:
                if neighb not in restable:
                    restable[neighb]=helper(neighb)
                reslist.append(restable[neighb])
            return False in reslist

        return helper(x)
                               

if __name__ == "__main__":
    g = GraphGame(6)
    g.add_link(3,4)
    g.add_link(1,4)
    g.add_link(4,5)
    print(g.winning(3)) # False
    print(g.winning(1)) # False
    g.add_link(3,1)
    g.add_link(4,6)
    g.add_link(6,5)
    print(g.winning(3)) # True
    print(g.winning(1)) # False
    print(g.winning(2)) # False
