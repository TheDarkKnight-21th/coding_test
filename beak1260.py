import sys
from collections import deque
def dfs(x):

    if visit_dfs[x] == False:
        visit_dfs[x] = True
        print(x , end=" ")
        for y in adj[x]:
            dfs(y)


def bfs(x):

    q=deque()
    q.append(x)

    while q:
        k = q.popleft()
        if visit_bfs[k] == False:
            visit_bfs[k] = True
            print(k,end= " ")

            for p  in adj[k]:
                q.append(p)


n ,m ,v = map(int,sys.stdin.readline().split())

adj = [[] for _ in range(n+1) ]

visit_dfs = [False for _ in range(n+1)]
visit_bfs = [False for _ in range(n+1)]

for _ in range(m):
    s,t = map(int,sys.stdin.readline().split())
    adj[s].append(t)
    adj[t].append(s)

for _ in adj:
    _.sort()

dfs(v)
print()
bfs(v)
