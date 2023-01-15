from math import inf
from heapq import heappush, heappop

def count(a,b,x):
    checked=set()
    amounts={(0,0): 0} #start state: both containers are empty and no water has been moved
    heap=[(0, 0, 0)]
    while len(heap)>0: #dijkstra's algorithm
        state=heappop(heap)[1:] #a state is a tuple whose elements corresponds to the amount of water in each container
        if state in checked:
            continue
        if state[0]==x: #algorithm finishes if we reach a state where there is the required amount of water in the first container
            return amounts[state]
        checked.add(state) #mark the state as checked
        missing=(a-state[0], b-state[1]) #calculate how much water is needed to fill each container
        neighbs=[(0, state[1], state[0]), (state[0], 0, state[1]), (a, state[1], missing[0]), (state[0], b, missing[1])] #there are six neighboring state. these four correspond to emptying or filling the containers
        if state[0]<=missing[1]: #the last two neighbors correspond to moving water between the containers. for this, we need to check whether the amount in each container is greater than the amount missing from the other
            neighbs.append((0, state[0]+state[1], state[0]))
        else:
            neighbs.append((state[0]-missing[1], b, missing[1]))
        if state[1]<=missing[0]:
            neighbs.append((state[0]+state[1], 0, state[1]))
        else:
            neighbs.append((a, state[1]-missing[0], missing[0]))
        for neighb in neighbs: #update the distances from initial state for each of the neighboring states, as per dijkstra's algorithm
            if neighb[:2] not in amounts:
                amounts[neighb[:2]]=inf
            currdist=amounts[neighb[:2]]
            newdist=amounts[state]+neighb[2]
            if newdist<currdist:
                amounts[neighb[:2]]=newdist
                heappush(heap, (newdist, neighb[0], neighb[1]))
    return -1
    

if __name__ == "__main__":
    print(count(5,4,2)) # 22
    print(count(4,3,2)) # 16
    print(count(3,3,1)) # -1
    print(count(10,9,8)) # 46
    print(count(123,456,42)) # 10530
