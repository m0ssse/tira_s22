def count(r):
    label=0
    visited=[[False]*len(r[0]) for i in range(len(r))]
    labels=[[-1]*len(r[0]) for i in range(len(r))]
    stack=[]
    for i in range(1, len(r)-1):
        for j in range(1, len(r[i])-1):
            row=i
            col=j
            stack.append((row, col))
            while len(stack)>0:
                row,col=stack.pop()
##                print(row, col)
                if visited[row][col] or r[row][col]=="#":
                    continue
                visited[row][col]=True
                neighbors=[(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
                maxlabel=max([labels[elem[0]][elem[1]] for elem in neighbors])
                if maxlabel>-1:
                    labels[row][col]=maxlabel
                else:
                    label+=1
                    labels[row][col]=label
                for neighbor in neighbors:
                    stack.append(neighbor)
##    [print(row) for row in labels]
    return label
                             
    
if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3
