class WallGrid:
    def __init__(self,n):
        self.grid=[[0]*(n+2) for _ in range(n+2)] #seinäruutuja kuvataan nollina, lattiaa ykkösinä
        self.compsize=[[0]*(n+2) for _ in range(n+2)]
        self.parent=[[(i, j) for j in range(n+2)] for i in range(n+2)]
        self.n=n
        self.rooms=0

##        self.print_grid(self.grid)
##        self.print_grid(self.parent)


    def repres(self, i, j):
        while (i, j)!=self.parent[i][j]:
            i, j=self.parent[i][j]
        return i, j

    def merge(self, i1, j1, i2, j2):
        i1, j1=self.repres(i1, j1)
        i2, j2=self.repres(i2, j2)
        if i1==i2 and j1==j2:
            return
        if self.compsize[i1][j1]<self.compsize[i2][j2]:
            i1,i2=i2,i1
            j1,j2=j2,j1
        self.parent[i2][j2]=(i1, j1)
        self.compsize[i1][j1]+=self.compsize[i2][j2]
        
        

    def print_grid(self, grid):
        [print(row) for row in grid]

    def remove(self,i,j):
        # TODO
        if self.grid[i][j]: #ruutu on jo lattiaa
            return
        self.grid[i][j]=1
        self.rooms+=1
        neighbs=[(i-1, j), (i+1, j), (i,j-1), (i,j+1)]
        for neighb in neighbs:
            i2, j2=neighb
            if not self.grid[i2][j2]:
                continue
            if self.repres(i, j)==self.repres(i2, j2):
                continue
            self.merge(i, j, i2, j2)
            self.rooms-=1
            

    def count(self):
        # TODO
       return self.rooms

if __name__ == "__main__":
    w = WallGrid(5)
    print(w.count()) # 0
    w.remove(2,2)
    w.remove(4,2)
    print(w.count()) # 2
    w.remove(3,2)
    print(w.count()) # 1
    w.remove(2,4)
    w.remove(2,4)
    w.remove(4,4)
    print(w.count()) # 3
    w.remove(3,3)
    print(w.count()) # 3
    w.remove(3,4)
    print(w.count()) # 1
