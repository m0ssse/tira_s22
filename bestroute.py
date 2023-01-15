from math import inf
from heapq import heappush, heappop

class BestRoute:
    def __init__(self,n):
        self.graph=[[] for _ in range(n+1)]

    def add_road(self,a,b,x):
        self.graph[a].append((b,x))
        self.graph[b].append((a,x))

    def find_route(self,a,b):
        dist=[inf]*len(self.graph)
        dist[a]=0
        visited=[False]*len(self.graph)
        found=False
        heap=[]
        heappush(heap, (0, a))
        while len(heap)>0:
            city=heappop(heap)[1]
            if city==b:
                return dist[b]
            if visited[city]:
                continue
            visited[city]=True
            for neighb in self.graph[city]:
                currdist=dist[neighb[0]]
                newdist=dist[city]+neighb[1]
                if newdist<currdist:
                    dist[neighb[0]]=newdist
                    heappush(heap, (newdist, neighb[0]))
        return -1
if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1,2,2)
    print(b.find_route(1,3)) # -1
    b.add_road(1,3,5)
    print(b.find_route(1,3)) # 5
    b.add_road(2,3,1)
    print(b.find_route(1,3)) # 3
