# https://www.acmicpc.net/problem/1238

'''
모든 노드에서 x로 도착할 때 걸리는 시간:
    visited를 공유해서 사용
+
x에서 각 노드로 돌아가는 시간

** 최단 시간에 오고가길 원한다 **

그냥 graph와 start와 end를 뒤집은 graph를 이용한다.
'''

import sys
import heapq
from math import inf
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = {i : dict() for i in range(1, n+1)} # {start: {end: time}, start2:...}
reverse_graph = {i : dict() for i in range(1, n+1)}

for _ in range(m):
    start, end, time = map(int, input().split())
    graph[start][end] = time
    reverse_graph[end][start] = time


def dijkstra(n, start, graph):
    dist_list = [inf for _ in range(n+1)] # -1이면 아직 방문하지 않음
    dist_list[start] = 0
    #visited = set()

    heap = [(0, start)]
    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_dist > dist_list[current_node]:
            continue

        for next_node, next_dist in graph[current_node].items():
            new_dist = dist_list[current_node] + next_dist

            if new_dist < dist_list[next_node]:
                dist_list[next_node] = new_dist
                heapq.heappush(heap, (next_dist, next_node))
    
    return dist_list

from_x = dijkstra(n, x, graph)
to_x = dijkstra(n, x, reverse_graph)
#print(from_x)
#print(to_x)

max_time = 0
for i in range(1, n+1):
    max_time = max(max_time, from_x[i] + to_x[i])

print(max_time)


