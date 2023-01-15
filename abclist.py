def create(n):
    strlist=[]
    chars="ABC"
    def fill(mystr, m):
        if len(mystr)==m:
            strlist.append(mystr)
            return
        for char in chars:
            newstr=mystr+char
            fill(newstr, n)
    fill("", n)
    return strlist
        
    

if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AA,AB,AC,BA,BB,BC,CA,CB,CC]
    print(len(create(5))) # 243
