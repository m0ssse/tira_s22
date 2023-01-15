class Cities:
    def __init__(self,n):
        self.citylist=[[] for _ in range(n+1)]
        
    def add_road(self,a,b):
        self.citylist[a].append(b)
        self.citylist[b].append(a)

    def has_route(self,a,b):
        visited=[]
        def helper(start, visitedcities):
            for city in self.citylist[start]:
                if city in visitedcities:
                    continue
                visitedcities.append(city)
                helper(city, visitedcities)
        helper(a, visited)
        return b in visited
                
            
        
            
if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1,2)
    c.add_road(1,3)
    c.add_road(4,5)
    print(c.has_route(1,5)) # False
    c.add_road(3,4)
    print(c.has_route(1,5)) # True
