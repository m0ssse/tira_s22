from math import inf

class AllRoutes:
    def __init__(self,n):
        self.distances=[[inf]*n for _ in range(n)]
        for i in range(n):
            self.distances[i][i]=0

    def add_road(self,a,b,x):
        self.distances[a-1][b-1]=min(self.distances[a-1][b-1], x)
        self.distances[b-1][a-1]=min(self.distances[b-1][a-1], x)
        
    def get_table(self):
        table=[row[:] for row in self.distances]
        for k in range(len(table)):
            for i in range(len(table)):
                for j in range(len(table)):
                    table[i][j]=min(table[i][j], table[i][k]+table[k][j])
        for i in range(len(table)):
            for j in range(len(table)):
                if table[i][j]==inf:
                    table[i][j]=-1
        return table

if __name__ == "__main__":
##    a = AllRoutes(4)
##    a.add_road(1,2,2)
##    a.add_road(1,3,5)
##    a.add_road(2,3,1)
##    print(a.get_table())
    # [[0,2,3,-1],[2,0,1,-1],[3,1,0,-1],[-1,-1,-1,0]]
    a = AllRoutes(5)
    a.add_road(3,4,6)
    a.add_road(4,5,5)
    a.add_road(4,5,6)
    a.add_road(1,5,7)
    a.add_road(1,4,7)
    a.add_road(4,5,1)
    a.add_road(3,4,8)
    a.add_road(2,3,6)
    a.add_road(4,5,4)
    print(a.distances)
    print(a.get_table())
