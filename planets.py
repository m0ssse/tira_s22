from collections import deque

class Planets:
    def __init__(self,n):
        self.edges_orig=[[0]*(n+1) for _ in range(n+1)]
        self.n=n

    def add_teleport(self,a,b):
        self.edges_orig[a][b]+=1

    def bfs(self, x, z, parents):
        visited=[False]*(self.n+1)
        visited[x]=True
        nodeorder=deque([x])
        found=False
        while len(nodeorder)>0:
            i=nodeorder.pop()
            for j in range(self.n+1):
                if self.edges[i][j]==0:
                    continue
                if visited[j]:
                    continue
                visited[j]=True
                nodeorder.append(j)
                parents[j]=i
        return visited[z]

    def calculate(self):
        x, z = 1, self.n
        self.edges=[row[:] for row in self.edges_orig]
        parents=[-1]*(self.n+1)
        flow=0
        while self.bfs(x, z, parents):
            pathedges=[]
            pathflow=10**9
            node=z
            while node!=x:
                pathedges.append((parents[node], node))
                pathflow=min(pathflow, self.edges[parents[node]][node])
                node=parents[node]
            flow+=pathflow
            pathedges=pathedges[::-1]
            for edge in pathedges:
                self.edges[edge[0]][edge[1]]-=pathflow
                self.edges[edge[1]][edge[0]]+=pathflow
        return flow

if __name__ == "__main__":
    p = Planets(5)
    print(p.calculate()) # 0
    p.add_teleport(1,2)
    p.add_teleport(2,5)
    print(p.calculate()) # 1
    p.add_teleport(1,5)
    print(p.calculate()) # 2
