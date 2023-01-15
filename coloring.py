class Coloring:
    def __init__(self,n):
        self.graph=[[] for i in range(n)]
        self.n=n
        

    def add_edge(self,a,b):
        self.graph[a-1].append(b-1)
        self.graph[b-1].append(a-1)

    def check(self):
        colors=[0]*self.n
        stack=[]
        for i in range(self.n):
            stack.append(i)
            while len(stack)>0:
                elem=stack.pop()
                if not colors[elem]:
                    colors[elem]=1
                for neighb in self.graph[elem]:
                    if not colors[neighb]:
                        colors[neighb]=-colors[elem]
                        stack.append(neighb)
                    elif colors[neighb]==colors[elem]:
                        return False
        return True
                
        

if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(3,4)
    c.add_edge(1,4)
    print(c.check()) # True
    c.add_edge(2,4)
    print(c.check()) # False
