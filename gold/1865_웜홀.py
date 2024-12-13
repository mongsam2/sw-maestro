# https://www.acmicpc.net/problem/1865

import sys
input = sys.stdin.readline

def bellman_ford(n, graph):
    dist = [1e4+1 for _ in range(n+1)]
    for iteration in range(n):

        for s, e, t in graph:
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t

                if iteration == n-1:
                    return True
                
    return False


tc = int(input())
for test_case in range(tc):
    #print("test_case", test_case)
    n, m, w = map(int, input().split())
    graph = []
    
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append([s, e, t])
        graph.append([e, s, t])

    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append([s, e, -t])

    #print(graph)
    #print(wormhole)
    minus_cycle = bellman_ford(n, graph)
    if minus_cycle:
        print("YES")
    else:
        print("NO")