def copygrid(grid: list):
    return [row[:] for row in grid]

def count(n, m, k):
    grid=[[0]*m]*n
    counter=[0]
    fillgrid(grid, 0, k, counter)
    return(counter[0])

def generate_rects(n, m):
    rectlist=[]
    for i in range(1, n+1):
        for j in range(1, m+1):
            rectlist.append((i*j, i, j))
    return sorted(rectlist, reverse=True)

def check_rect(grid: list, rect: tuple, row: int, col: int):
    endrow=row+rect[1]-1
    endcol=col+rect[2]-1
    if row+rect[1]-1>=len(grid) or col+rect[2]-1>=len(grid[0]): #check if the rectangle goes past the grid boundaries
        return False
    for i in range(row, row+rect[1]): #check that none of the squares are already occupied
        for j in range(col, col+rect[2]):
            if grid[i][j]:
                return False
    return True

def add_rect(grid: list, rect: tuple, row: int, col: int, val=1):
    for i in range(row, row+rect[1]):
        for j in range(col, col+rect[2]):
            grid[i][j]=val
    return True

def printgrid(grid):
    for row in grid:
        print(row)
    print()

def fillgrid(grid: list, startpos: int, N: int, counter: list):
    #fills the grid with rectangles starting from position startpos. linear indexing is used for positions
    #N is the maximum number of rectangles that should be added
    n=len(grid)
    m=len(grid[0])
    if N==0 or startpos>=m*n:
        if min([min(gridrow) for gridrow in grid])>0:
            counter[0]+=1
        return
    row=startpos//m
    col=startpos%m
    rectlist=generate_rects(n-row+1, m-col+1)
    for rect in rectlist:
        if check_rect(grid, rect, row, col):
            copy=copygrid(grid)
            add_rect(copy, rect, row, col)
            newpos=startpos
            while True:
                newrow=newpos//m
                newcol=newpos%m
                if newpos==m*n or copy[newrow][newcol]==0:
                    break
                newpos+=1
            fillgrid(copy, newpos, N-1, counter)
    

if __name__ == "__main__":
##    pass
##    grid=[4*[0] for i in range(4)]
##    printgrid(grid)
##    add_rect(grid, (9, 3, 3), 0, 0)
##    printgrid(grid)
##    print(add_rect(grid, (3, 3, 1), 0, 3))
##    printgrid(grid)
##    print(generate_rects(4, 4))
##    print(count(2, 3, 3)) #13
##    print(count(2,2,4)) # 8
##    print(count(2,3,3)) # 13
##    print(count(4,4,1)) # 1
##    print(count(4,3,10)) # 3146
    print(count(4,4,16)) # 70878
