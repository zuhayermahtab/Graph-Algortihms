# python3
import sys


def explore(adj,x,visited,precout,postcout,clock):
        visited[x]=1
        precout[x]=clock
        clock+=1
        for i in adj[x]:
            if visited[i]==0:
                clock=explore(adj,i,visited,precout,postcout,clock)
        postcout[x]=clock
        clock+=1
        return clock
def toposort(adj):
    visited=[0]*n
    precout=[0]*n
    postcout=[0]*n
    clock=0
    order = [0]*n
    for x in range(0,n):
        if visited[x]==0:
            clock=explore(adj,x,visited,precout,postcout,clock)
    order=sorted(range(len(postcout)),key=lambda k: postcout[k],reverse=True)
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

