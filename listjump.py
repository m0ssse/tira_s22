from math import inf
from heapq import heappush, heappop

def calculate(t):
    graph=[[] for _ in range(len(t))]
    for i in range(len(graph)):
        if i-t[i]>=0:
            graph[i].append((i-t[i], t[i]))
        if i+t[i]<len(graph):
            graph[i].append((i+t[i], t[i]))
    dist=[inf]*len(graph)
    dist[0]=0
    visited=[False]*len(graph)
    heap=[(0, 0)]
    while len(heap)>0:
        elem=heappop(heap)[1]
        if elem==len(t)-1:
            return dist[-1]
        if visited[elem]:
            continue
        visited[elem]=True
        for neighb in graph[elem]:
            currdist=dist[neighb[0]]
            newdist=dist[elem]+neighb[1]
            if newdist<currdist:
                dist[neighb[0]]=newdist
                heappush(heap, (newdist, neighb[0]))
    return -1

if __name__ == "__main__":
    print(calculate([1,1,1,1])) # 3
    print(calculate([3,2,1])) # -1
    print(calculate([3,5,2,2,2,3,5])) # 10
    print(calculate([7,5,3,1,4,2,4,6,1])) # 32
