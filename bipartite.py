#python3

import sys
from queue import Queue

def bfs(adj,s):
    dist[s]=0
    q.put(s)
    color[s]=1
    while q.empty()==False:
        u=q.get()
        for v in adj[u]:
            if dist[v]=="NaN":
                q.put(v)
                dist[v]=dist[u]+1
                color[v]=1-color[u]
            elif color[v]==color[u]:
                return 0
    return 1
def bipartite(adj):
    s=0
    return bfs(adj,s)
    

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    dist=["NaN"]*n
    q=Queue(maxsize=n)
    color=[-1]*n
    print(bipartite(adj))
