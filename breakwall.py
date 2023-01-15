from heapq import heappush, heappop
from math import inf

def find(grid, char):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]==char:
                return i, j

def count(r):
    startpos=find(r, "A")
    goalpos=find(r, "B")
    visited=set()
    wallbreaks={}
    wallbreaks[startpos]=0
    heap=[(0, startpos[0], startpos[1])]
    while len(heap)>0:
        i,j=heappop(heap)[1:]
        if (i, j) in visited:
            continue
        if i==goalpos[0] and j==goalpos[1]:
            return wallbreaks[goalpos]
        visited.add((i,j))
        neighbs=[(i-1,j), (i+1, j), (i, j-1), (i, j+1)]
        for square in neighbs:
            row,col=square[0], square[1]
            if r[row][col]=="#":
                continue
            if square not in wallbreaks:
                wallbreaks[square]=inf
            currdist=wallbreaks[square]
            if r[row][col]=="*":
                newdist=wallbreaks[(i,j)]+1
            else:
                newdist=wallbreaks[(i,j)]
            if newdist<currdist:
                wallbreaks[square]=newdist
                heappush(heap, (wallbreaks[square], row, col))
    return -1
                
        
    
    
if __name__ == "__main__":
    r = ["########",
         "#*A*...#",
         "#.*****#",
         "#.**.**#",
         "#.*****#",
         "#..*.B.#",
         "########"]
    print(count(r)) # 2
