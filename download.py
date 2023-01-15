from collections import deque

class Download:
    def __init__(self,n):
        self.edges_orig=[[0]*(n+1) for _ in range(n+1)]
        self.n=n

    def add_link(self,a,b,x):
        self.edges_orig[a][b]+=x

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

    def calculate(self, x, z):
        self.edges=[row[:] for row in self.edges_orig]
        parents=[-1]*(self.n+1)
        flow=0
        while self.bfs(x, z, parents): #jos metodi bfs palauttaa True, on täydennyspolku löytynyt
            pathedges=[]
            pathflow=10**9
            node=z
            while node!=x: #tarkistetaan lähtien polun loppupäästä missä solmuissa on käyty
                pathedges.append((parents[node], node)) #lisätään polun kaaret listalle käänteisessä järjestyksessä
                pathflow=min(pathflow, self.edges[parents[node]][node]) #päivitetään pienimmän kaaren painoa polulla
                node=parents[node]
            flow+=pathflow #lisätään virtausta pienimmän virtauksen verran 
            pathedges=pathedges[::-1]
            for edge in pathedges:
                self.edges[edge[0]][edge[1]]-=pathflow
                self.edges[edge[1]][edge[0]]+=pathflow
        return flow

if __name__ == "__main__":
    d = Download(4)
    print(d.calculate(1,4)) # 0
    d.add_link(1,2,5)
    d.add_link(2,4,6)
    d.add_link(1,4,2)
    print(d.calculate(1,4)) # 7
    d.add_link(1,3,4)
    d.add_link(3,2,2)
    print(d.calculate(1,4)) # 8
