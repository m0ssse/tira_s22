from collections import deque

class Ball:
    def __init__(self,n):
        self.edges_orig=[[0]*(2*n+2) for _ in range(2*n+2)]
        self.n=2*n+1
        for i in range(1, n+1):
            self.edges_orig[0][i]+=1
            self.edges_orig[i+n][2*n+1]+=1
        

    def add_pair(self,a,b):
##        [print(line) for line in self.edges_orig]
        b+=(self.n-1)//2
##        print(a)
##        print(b)
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
        x, z = 0, self.n
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
    b = Ball(4)
    print(b.calculate()) # 0
    b.add_pair(1,2)
    print(b.calculate()) # 1
    b.add_pair(1,3)
    b.add_pair(3,2)
    print(b.calculate()) # 2
