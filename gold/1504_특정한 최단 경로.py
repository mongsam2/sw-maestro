# https://www.acmicpc.net/problem/1504
'''
그래프 이론
최단 경로
데이크스트라
'''

import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())
graph = {i: dict() for i in range(1, n+1)}

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

v1, v2 = map(int, input().split())

def dijkstra(start, graph):
    dist_list = [float("inf") for _ in range(len(graph.keys())+1)]
    heap = [(0, start)]
    dist_list[start] = 0

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        # 현재 노드에 도착하기까지 걸렸던 총 비용 > 출발 노드로부터 현재 노드까지의 최단거리
        # 확인할 필요가 없으니, 힙에서 제외. 앞으로도 힙에 포함될 일 없음음
        if current_dist > dist_list[current_node]: 
            continue

        for next_node, next_dist in graph[current_node].items():
            new_dist = current_dist + next_dist

            if new_dist < dist_list[next_node]:
                dist_list[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    return dist_list

one_to = dijkstra(1, graph)
n_to = dijkstra(n, graph)
v1_to_v2 = dijkstra(v1, graph)[v2]

path1 = one_to[v1] + n_to[v2]
path2 = one_to[v2] + n_to[v1]
answer = min(path1, path2) + v1_to_v2
if answer == float("inf"):
    print(-1)
else:
    print(answer)
