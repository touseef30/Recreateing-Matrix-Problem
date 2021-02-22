

U=3
L=2
C = [2,1,1,0,1]
def solution(U, L, C):
    
    idx = 0
    result = list()
    l = len(C)
    u0 = []
    l1 = []
    for i in range(l):
        u0.append(i*0)
    for i in range(l):
        l1.append(i*0)

    total = sum(C) 
    if total != U+L:
        return "IMPOSSIBLE"
    else:
        for x in C:
            if x==2:
                u0[idx] = 1
                l1[idx] = 1
                idx+=1
            if x == 0:
                u0[idx] = 0
                l1[idx] = 0
                idx+=1
            if x == 1:
                sum0 = sum(u0)
                if sum0 < U:
                    u0[idx] = 1
                    l1[idx] = 0
                    sum0+=1
                else:
                    u0[idx] = 0
                    l1[idx] = 1
                idx+=1
    first = ""
    second = ""
    for i in u0:
        first = first + str(i)
    for j in l1:
        second = second + str(j)

    return first+","+second

print(solution(U, L, C))
