#python3

import sys
def explore(adj,x,visited,restack):
        visited[x]=1
        restack[x]=1
        for i in adj[x]:
            if visited[i]==0:
                if explore(adj,i,visited,restack)==1:
                    return 1
            elif restack[i]==1:
                    return 1
        restack[x]=0
        return 0
                
def acyclic(adj,n):
    visited=[0]*n
    restack=[0]*n
    for x in range(0,n):
        if visited[x]==0:
            if explore(adj,x,visited,restack)==1:
                return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj,n))
    