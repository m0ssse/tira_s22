def create(n):
    strlist=[]
    chars="ABC"
    def fill(mystr, m):
        if len(mystr)==m:
            strlist.append(mystr)
            return
        for char in chars:
            if mystr and mystr[-1]==char:
                continue
            newstr=mystr+char
            fill(newstr, n)
    fill("", n)
    return strlist

if __name__ == "__main__":
    print(create(1)) # [A,B,C]
    print(create(2)) # [AB,AC,BA,BC,CA,CB]
    print(len(create(5))) # 48
