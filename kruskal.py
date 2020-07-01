#Uses python3
import sys
import math

def minimum_distance(resultset):
    result = 0.
    for (u,v,w) in resultset:
        result+=w
    return result
def kruskal():
    for i in range(n):
        makeset(i)
    for ((u,v),w) in edges:
        if find(u)!=find(v):
            z=(u,v,w)
            resultset.append(z)
            union(u,v)
    return resultset

def makeset(i):
    parent[i]=i
    rank[i]=0

def find(i):
    while i!=parent[i]:
        i=parent[i]
    return i
def union(i,j):
    i_id=find(i)
    j_id=find(j)
    if i_id==j_id:
        return
    if rank[i_id]>rank[j_id]:
        parent[j_id]=i_id
    else:
        parent[i_id]=j_id
        if rank[i_id]==rank[j_id]:
            rank[j_id]=rank[j_id]+1

def sortingkey(elem):
    return elem[1]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    edges=[]
    for i in range(n-1):
        for j in range(i+1,n):
            dist=math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
            p=((i,j),dist)
            edges.append(p)
    edges.sort(key=sortingkey)
    resultset=[]
    rank=[0]*n
    parent=[0]*n
    print(kruskal())
    print("{0:.9f}".format(minimum_distance(resultset)))