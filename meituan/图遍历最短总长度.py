# encoding: utf-8

N = int(input())

graph = list([0] * (N+1) for i in range(N+1))
for i in range(N-1):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1
print(graph)
visited = [0] * (N+1)
depth = [0] * (N+1)

queue = [1]
visited[1] = 1

while queue:
    cur_po = queue.pop(0)
    for i in range(len(graph[cur_po])):
        if graph[cur_po][i] == 1 and visited[i] != 1:
            visited[i] = 1
            queue.append(i)
            depth[i] = depth[cur_po] + 1

print(2*(N-1)-max(depth))




