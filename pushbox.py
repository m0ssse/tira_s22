from collections import deque

def find_square(r, char):
    for i in range(len(r)):
        for j in range(len(r[0])):
            if r[i][j]==char:
                return i,j

def move(ix, jx, ib, jb, direction, r):
    #TODO tarkista että boksi on oikeasti kohderuudussa äläkä oio
    ix_new=ix
    jx_new=jx
    ib_new=ib
    jb_new=jb
    if direction=="U":
        ix_new-=1
        if ix_new==ib_new and jx_new==jb_new:
            ib_new-=1
    if direction=="D":
        ix_new+=1
        if ix_new==ib_new and jx_new==jb_new:
            ib_new+=1
    if direction=="L":
        jx_new-=1
        if ix_new==ib_new and jx_new==jb_new:
            jb_new-=1
    if direction=="R":
        jx_new+=1
        if ix_new==ib_new and jx_new==jb_new:
            jb_new+=1
    if r[ix_new][jx_new]=="#" or r[ib_new][jb_new]=="#": #if the new position of X or the box is a wall, return the original coordinates
        return ix, jx, ib, jb
    return ix_new, jx_new, ib_new, jb_new
            
def count(r):
    ix, jx = find_square(r, "X")
    ib, jb = find_square(r, "B")
    iy, jy = find_square(r, "Y")
    initpos=(ix, jx, ib, jb)
    visited=set()
    visited.add(initpos)
    dist={}
    dist[initpos]=0
    queue=deque()
    queue.append(initpos)
##    solfound=False
    counter=1
    while len(queue)>0:
        state=queue.popleft()
        ix, jx, ib, jb = state[0], state[1], state[2], state[3]
        neighborlist=[]
        for char in "UDLR":
##            print(f"X in {ix} {jx} box in {ib} {jb} moving {char}")
##            counter+=1
            ix_new, jx_new, ib_new, jb_new=move(ix, jx, ib, jb, char, r)
##            print(f"new pos: X in {ix_new} {jx_new} box in {ib_new} {jb_new}")
            if (ix_new, jx_new, ib_new, jb_new) in visited:
                continue
##            print(f"X in {ix} {jx} box in {ib} {jb}")
##            print(f"moving {char}")
##            print(f"new pos:")
##            print(f"X in {ix_new} {jx_new} box in {ib_new} {jb_new}")
##            print()
##            print(f"trying X in {ix_new}, {jx_new} box in {ib_new}, {jb_new}")
            queue.append((ix_new, jx_new, ib_new, jb_new))
            visited.add((ix_new, jx_new, ib_new, jb_new))
            dist[(ix_new, jx_new, ib_new, jb_new)]=dist[(ix, jx, ib, jb)]+1
            if ib_new==iy and jb_new==jy:
                return dist[(ix_new, jx_new, ib_new, jb_new)]
    return -1
    

if __name__ == "__main__":
    r = ["########",
         "#......#",
         "#.#.Y#.#",
         "#.#B.#.#",
         "#..X.#.#",
         "#.#..#.#",
         "########"]
##    print(move(2, 3, 3, 3, "D", r))
    print(count(r)) # 18
