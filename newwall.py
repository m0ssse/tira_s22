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
        self.neighbs[a].append(b)

    def remove_edge(self, a, b):
        if (a,b) in self.edges:
            self.edges.pop(a,b)
            self.edges.pop(b,a)
            self.neighbs[a].remove(b)

    def bfs(self, x, z):
        visited={}
        visited[x]=True
        queue=deque([x])
        while len(queue)>0:
            vertex=queue.pop()
##            print(f"checking {vertex}")
            if vertex==z:
##                print("Found!")
##                print(parents)
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
        return False

def count(r):
    graph=Graph()
    n=len(r)
    r_padded=["#"*(n+2)]
    for row in r:
        r_padded.append("#"+row+"#")
    r_padded.append("#"*(n+2))
    aslist=[list(row) for row in r_padded]
    for i in range(1,n+1):
        for j in range(1, n+1):
            if r_padded[i][j]=="#":
                continue
            neighbs=[(i+1,j), (i, j+1)]
            for neighb in neighbs:
                if r_padded[neighb[0]][neighb[1]]=="#":
                    continue
##                print(f"adding edge between {(i,j)} and {neighb}")
                graph.add_edge((i,j),neighb)
    #if there is no path to the bottom right corner, then no walls need to be added
    if not graph.bfs((1,1),(n,n)):
        return 0
    #check each square in the grid and turn it into a wall. then check if a path can be found and change it back
    #if a square is found where this removes any path to the bottom-right corner, return 1
    #if no square has this property, return 2
    for i in range(1, n**2-1):
        row, col = i//n+1, i%n+1
        if r_padded[row][col]=="#":
            continue
        parents=[(row-1, col), (row, col-1)] 
        children=[(row+1, col), (row, col+1)]
        for parent in parents:
            if r_padded[parent[0]][parent[1]]=="#":
                continue
            graph.remove_edge(parent, (row, col))
        for child in children:
            if r_padded[child[0]][child[1]]=="#":
                continue
            graph.remove_edge((row, col), child)
        if not graph.bfs((1,1),(n,n)):
            return 1
        for parent in parents:
            if r_padded[parent[0]][parent[1]]=="#":
                continue
            graph.add_edge(parent, (row, col))
        for child in children:
            if r_padded[child[0]][child[1]]=="#":
                continue
            graph.add_edge((row, col), child)
    return 2
        
        

if __name__ == "__main__":
    r=[".#...",
       "....#",
       "..#..",
       ".....",
       "....."]
##    r=[".#...",
##       "....#",
##       "..#..",
##       ".....",
##       "....."]
##    r = [".....",
##         ".###.",
##         "...#.",
##         "##.#.",
##         "....."]
    print(count(r)) # 2
