from collections import deque

class Network:
    def __init__(self,n):
        self.nodelist=[[] for _ in range(n+1)]
        self.n=n

    def add_link(self,a,b):
        self.nodelist[a].append(b)
        self.nodelist[b].append(a)

    def best_route(self,a,b):
        dist=[-1 for _ in range(self.n+1)]
        dist[a]=0
        visited=[False for _ in range(self.n+1)]
        fifo=deque()
        fifo.append(a)
        while len(fifo)>0:
            city=fifo.popleft()
            for neighbor in self.nodelist[city]:
                if visited[neighbor]:
                    continue
                fifo.append(neighbor)
                visited[neighbor]=True
                dist[neighbor]=dist[city]+1
        return dist[b]
                
            

if __name__ == "__main__":
    w = Network(5)
    w.add_link(1,2)
    w.add_link(2,3)
    w.add_link(1,3)
    w.add_link(4,5)
    print(w.best_route(1,5)) # -1
    w.add_link(3,5)
    print(w.best_route(1,5)) # 2
