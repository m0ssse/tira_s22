from collections import deque

class Graph:
    def __init__(self):
        self.edges={}
        self.neighbs={}

    def add_edge(self, a, b):
        if (a,b) not in self.edges:
            self.edges[(a,b)]=0
        if (b,a) not in self.edges:
            self.edges[(b,a)]=0
        self.edges[(a,b)]+=1
        if not a in self.neighbs:
            self.neighbs[a]=[]
        if not b in self.neighbs:
            self.neighbs[b]=[a]
        self.neighbs[a].append(b)
        self.neighbs[b].append(a)

    def bfs(self, x, z, parents):
        visited={}
        visited[x]=True
        queue=deque([x])
        found=False
        while len(queue)>0:
            vertex=queue.pop()
            if vertex==z:
                return True
            if not vertex in self.neighbs:
                continue
            for neighb in self.neighbs[vertex]:
                if self.edges[(vertex, neighb)]==0:
                    continue
                if neighb in visited:
                    continue
                visited[neighb]=True
                queue.append(neighb)
                parents[neighb]=vertex
        return False

    def maxflow(self, x, z):
        parents={}
        flow=0
        while self.bfs(x, z, parents):
            pathedges=[]
            pathflow=10**9
            node=z
            while node!=x:
                pathedges.append((parents[node], node))
                pathflow=min(pathflow, self.edges[(parents[node],node)])
                node=parents[node]
            flow+=pathflow
            pathedges=pathedges[::-1]
            for edge in pathedges:
                self.edges[(edge[0],edge[1])]-=1
                self.edges[(edge[1],edge[0])]+=1
##            print(pathedges)
        return flow
    
def pad(r):
    n=len(r)
    r_padded=["#"*(n+2)]
    for row in r:
        r_padded.append("#"+row+"#")
    r_padded.append("#"*(n+2))
    return r_padded

def count(r):
    graph=Graph()
    r_padded=pad(pad(r))
##    [print(row) for row in r_padded]
    leftlist=[]
    rightlist=[]
    for i in range(2, 10):
        for j in range(2+i%2, 10, 2):
            #tarkastetaan vain "valkoiset" ruudut, jotta kaaret saadaan suunnattua oikein.
            #jos kaksi ratsua n??kev??t toisensa, toinen ratsu on v??ist??m??tt?? valkoisessa ja toinen mustassa ruudussa. t??st?? saadaan luonnostaan kaksijakoinen verkko
            #n??in varmistetaan my??s, ett?? jos kaksi ratsua n??kev??t toisensa, n??iden solmujen v??lille lis??t????n kaari vain kerran
            if not r_padded[i][j]=="*":
                continue
            neighbs=[(i+2, j+1),(i+2, j-1),(i+1, j+2),(i+1, j-2),(i-2, j+1),(i-2, j-1),(i-1, j+2),(i-1, j-2)]
            square=(i,j)
            graph.add_edge((0,0), square) #solmu (0,0) vastaa virtauksen l??hdett??
            for neighb in neighbs:
                if r_padded[neighb[0]][neighb[1]]=="*":
                    graph.add_edge(square, neighb)
                    if (neighb, (10, 10)) not in graph.edges: #tarkistetaan onko mustassa ruudussa olevasta ratsusta jo kaari virtauksen p????tepisteeseen
                        graph.add_edge(neighb, (10, 10))
    return graph.maxflow((0,0), (10, 10))
    
            

if __name__ == "__main__":
    r = ["*.......",
         "..*...*.",
         "........",
         ".*......",
         "...*....",
         ".......*",
         "........",
         "......*."]
    print(count(r)) # 3
