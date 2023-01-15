from collections import deque

def find_start(r):
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j]=="A":
                return i, j

def find_end(r):
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j]=="B":
                return i, j
def count(r):
    # TODO
    stack=deque()
    start=find_start(r)
    stack.append(start)
    end=find_end(r)
    visited=[[False]*len(r[0]) for _ in r]
    dist=[[-1]*len(r[0]) for _ in r]
    visited[start[0]][start[1]]=True
    dist[start[0]][start[1]]=0
    while len(stack)>0:
        square=stack.popleft()
        row,col=square[0],square[1]
        neighbors=[(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for neighbor in neighbors:
            i, j=neighbor[0], neighbor[1]
            if visited[i][j] or r[i][j]=="#":
                continue
            stack.append(neighbor)
            visited[i][j]=True
            dist[i][j]=dist[row][col]+1
    return dist[end[0]][end[1]]

if __name__ == "__main__":
    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]
    print(count(r)) # 7
