import sys

def dfs(x,y,a,b,thr):
    global result


    if (x >= 0 and x < n) and (y >= 0 and y < n):

        if not visit[x][y]:
            if graph[x][y] < thr:
                return False

            if visit[a][b] == 0:
                result += 1

            visit[x][y] = True
            dfs(x+1,y,x,y,thr)
            dfs(x ,y+1,x,y,thr)
            dfs(x-1, y,x,y,thr)
            dfs(x, y-1,x,y,thr)

sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

graph = []
visit= [[False]*n for i in range(n)]
result = 0
threshold = []
ans = []

for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

for i in range(n):
    for j in range(n):
        if not ( graph[i][j] in threshold):
            threshold.append(graph[i][j])

for thrs in threshold:
    visit = [[False] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            dfs(i,j,i,j,thrs)

    ans.append(result)
    result = 0

print(max(ans))


