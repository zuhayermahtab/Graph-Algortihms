#Uses python3

import sys
def explore(adj,x,cc):
        visited[x]=1
        ccnum[x]=cc
        for i in adj[x]:
            if visited[i]==0:
                x=i
                explore(adj,x,cc)

def number_of_components(adj):
    result = 0
    #write your code here
    
    cc=1
    for x in range(0,n):
        if visited[x]!=1:
            explore(adj,x,cc)
            cc+=1
    result=cc-1
    return result

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
    visited=[0]*n
    ccnum=[0]*n
    print(number_of_components(adj))
