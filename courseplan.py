class CoursePlan:
    def __init__(self):
        self.graph={}
        

    def add_course(self,course):
        self.graph[course]=[]

    def add_requisite(self,course1,course2): #course1 on kurssin course2 esitietovaatimus
        self.graph[course1].append(course2)

    def find(self):
        self.order=[]
        self.status={course: 0 for course in self.graph}
        self.cycle=False

        def helper(course):
            if self.cycle:
                return
            if self.status[course]==2:
                return
            if self.status[course]==1:
                self.cycle=True
                return
            self.status[course]=1
            for nextcourse in self.graph[course]:
                helper(nextcourse)
            self.status[course]=2
            self.order.append(course)
        for course in self.graph:
            if self.status[course]==0:
                helper(course)
        if self.cycle:
            return None
        return self.order[::-1]

if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe","Ohja")
    c.add_requisite("Ohja","Tira")
    c.add_requisite("Jym","Tira")
    print(c.find()) # [Ohpe,Jym,Ohja,Tira]
    c.add_requisite("Tira","Tira")
    print(c.find()) # None
