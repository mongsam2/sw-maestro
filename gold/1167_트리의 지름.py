# https://www.acmicpc.net/problem/1167
# 트리
'''
그래프 이론
그래프 탐색
트리
깊이 우선 탐색
'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v = int(input())
tree = {i: dict() for i in range(1, v+1)} # {node: {node: dis, node: dis}}   
max_length = 0

for _ in range(v):
    #print("node", _)
    info = list(map(int, input().split()))
    node, edges = info[0], info[1:-1]
    #print("edges", edges)

    for i in range(0, len(edges)-1, 2):
        edge, distance = edges[i], edges[i+1]
        tree[node][edge] = distance


def dfs(now, tree, visited, dist): # dist: [*, 0, 0, 1]

    '''
    dist: 임의의 노드로 부터 각 노드가 떨어진 거리를 저장
    '''

    for next_node in tree[now].keys():
        if visited[next_node] == -1:
            new_dist = dist + tree[now][next_node]
            visited[next_node] = new_dist
            dfs(next_node, tree, visited, new_dist)

    
one_visited = [-1 for _ in range(v+1)]
one_visited[1] = 0
dfs(1, tree, one_visited, 0)
start_node = one_visited.index(max(one_visited))
#print(one_visited)

visited = [-1 for _ in range(v+1)]
visited[start_node] = 0
dfs(start_node, tree, visited, 0)
length = max(visited)
#print(visited)

print(length)

#print(finish_search)
'''
2 - 4 - 5
    |
    3 - 1
'''