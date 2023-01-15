from collections import deque

class Graph:
    def __init__(self):
        self.edges={}
        self.neighbs={}

    def add_edge(self, a, b, x):
        if (a,b) not in self.edges:
            self.edges[(a,b)]=0
        if (b,a) not in self.edges:
            self.edges[(b,a)]=0
        self.edges[(a,b)]+=x
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
    r_padded=pad(r)
    n=len(r)
    graph=Graph()
    rowcounts=[0]*(n+1)
    colcounts=[0]*(n+1)
    for i in range(1, n+1):
        for j in range(1, n+1):
            if r_padded[i][j]=="X":
                graph.add_edge((i,0),(i,j),1)
                graph.add_edge((i,j),(0,j),1)
                rowcounts[i]+=1
                colcounts[j]+=1
    for i in range(1, n+1):
        graph.add_edge((0,0),(i,0),1)
        graph.add_edge((0,i),(n+1,n+1), 1)
##        graph.add_edge((0,0),(i,0),rowcounts[i])
##        graph.add_edge((0,i),(n+1,n+1), colcounts[i])
    return graph.maxflow((0,0),(n+1,n+1))
##    for i in range(1, n+1)

if __name__ == "__main__":
    r =["........",
        "........",
        "...X..X.",
        "........",
        "....X...",
        "..X.X..X",
        "........",
        "....X..."]
    print(count(r)) # 3
    
