from math import inf

class Shortening:
    def __init__(self,n):
        self.n=n
        self.graph=[[inf]*n for _ in range(n)]
        for i in range(self.n):
            self.graph[i][i]=0

    def add_edge(self,a,b,x):
        self.graph[a-1][b-1]=min(self.graph[a-1][b-1], x)

    def check(self, a, b):
        distmat=[row[:] for row in self.graph]
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    distmat[i][j]=min(distmat[i][j], distmat[i][k]+distmat[k][j])
        if distmat[a-1][b-1]==inf:
            return False
        for i in range(self.n):
            if distmat[i][i]<0 and distmat[a-1][i]<inf and distmat[i][b-1]<inf:
                return True
        return False

##    def check(self,a,b):
##        counter=0
##        dist=[inf]*(self.n+1)
##        dist[a]=0
##        while True:
##            muutos=False
####            print(counter)
##            if counter>=self.n:
##                return True
##            for edge in self.edges:
##                currdist=dist[edge[1]]
##                newdist=dist[edge[0]]+edge[2]
##                if newdist<currdist:
##                    dist[edge[1]]=newdist
##                    muutos=True
##            counter+=1
##            if not muutos:
##                break
##        return False

if __name__ == "__main__":
    s = Shortening(5)
    print(s.check(1,3)) # False
    s.add_edge(1,2,5)
    s.add_edge(2,3,-2)
    print(s.check(1,3)) # False
    s.add_edge(2,4,1)
    s.add_edge(4,2,-2)
    print(s.check(1,3)) # True
