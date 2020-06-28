#Uses python3

import sys
import math


    
    
def negative_cycle(edges):
    for i in range(n-1):
        for ((u,v),w) in edges:
            if dist[v-1]>dist[u-1]+w:
                dist[v-1]=dist[u-1]+w
    for ((u,v),w) in edges:
        if dist[v-1]>dist[u-1]+w:
            return 1
        else:
            return 0


if __name__ == '__main__':
    input =sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    dist=[math.inf]*n
    dist[0]=0
    print(negative_cycle(edges))
    print(dist)
