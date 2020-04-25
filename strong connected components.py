# python3
import sys
sys.setrecursionlimit(200000)

def explore(radj,x,visited,precout,postcout,clock):
        visited[x]=1
        precout[x]=clock
        clock+=1
        for i in radj[x]:
            if visited[i]==0:
                clock=explore(radj,i,visited,precout,postcout,clock)
        postcout[x]=clock
        clock+=1
        return clock
def toposort(radj):
    visited=[0]*n
    precout=[0]*n
    postcout=[0]*n
    clock=0
    order = [0]*n
    for x in range(0,n):
        if visited[x]==0:
            clock=explore(radj,x,visited,precout,postcout,clock)
    order=sorted(range(len(postcout)),key=lambda k: postcout[k],reverse=True)
    return order
def scc(adj):
    order=toposort(radj)
    cc=1
    for x in order:
        if visited2[x]!=1:
            explore2(adj,x,cc)
            cc+=1
    result=cc-1
    return result
def explore2(adj,x,cc):
        visited2[x]=1
        ccnum[x]=cc
        for i in adj[x]:
            if visited2[i]==0:
                x=i
                explore2(adj,x,cc)    
    
    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    radj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        radj[b-1].append(a-1)
    visited2=[0]*n
    ccnum=[0]*n
    result=scc(adj)
    print(result)

