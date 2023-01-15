class LongPath:
    def __init__(self,n):
        self.graph=[[] for _ in range(n+1)]
        self.n=n

    def add_edge(self,a,b):
        self.graph[a].append(b)
        self.graph[b].append(a)
        
    def calculate(self):
        maxlength=0
        pathlengths=[1]*(self.n+1)
        for i in range(1, self.n+1):
##            print(f"lengths so far: {pathlengths}")
##            print(f"checking vertex {i}")
            longest=0
            for neighb in self.graph[i]:
                if neighb<i:
                    longest=max(longest, pathlengths[neighb])
                pathlengths[i]=longest+1
                maxlength=max(maxlength, longest+1)
        return max(0, maxlength-1)
                

if __name__ == "__main__":
    l = LongPath(4)
    l.add_edge(1,2)
    l.add_edge(1,3)
    l.add_edge(2,4)
    l.add_edge(3,4)
    print(l.calculate()) # 2
    l.add_edge(3,2)
    print(l.calculate()) # 3
