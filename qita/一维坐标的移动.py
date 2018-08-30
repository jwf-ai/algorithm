# encoding: utf-8
from queue import Queue

def bfs(start,end,n):
    q = Queue()
    q.put((start,0))
    visit = [0] * (n+1)
    visit[start] = 1

    D = [0] * (n+1)
    P = [0] * (n+1)

    while q.empty() != True:

        dist, num = q.get()

        if dist == end:
            return num,D,P
        else:
            dist_tmp = 0
            for i in range(3):
                if i == 0:
                    dist_tmp = dist - 1
                elif i == 1:
                    dist_tmp = dist + 1
                else:
                    dist_tmp = dist * 2

                if dist_tmp>=0 and dist_tmp<=n and visit[dist_tmp] == 0:
                    q.put((dist_tmp, num+1))
                    visit[dist_tmp] = 1
                    P[dist_tmp] = dist
                    D[dist_tmp] = D[dist] + 1
    return None

def showPath(start,end,parent):
    res = []
    tmp = end
    while tmp != start:
        res.append(tmp)
        tmp = parent[tmp]
    res.append(start)
    res.reverse()
    return res


num,D,P = bfs(0,13,16)

print("num:",num)
print(showPath(0,13,P))


