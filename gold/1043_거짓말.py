# https://www.acmicpc.net/problem/1043
# bfs
# greedy
# set

'''
자료 구조
그래프 이론
그래프 탐색
분리 집합
'''

from collections import deque

def make_graph(n:int, party_list:list[tuple]):
    '''
    n: 총 사람의 수
    party_list: 파티들의 정보를 담은 list (파티에 온 사람, 사람들의 리스트)

    return: 파티에서 한 번이라도 만난 사람들을 연결한 그래프
    '''
    graph = {i+1: set() for i in range(n)}
    for _, people in party_list:
        for person in people:
            graph[person].update(people)
    return graph

def bfs(start:int, edges:dict[int, list]) -> set:
    '''
    start: 탐색을 시작할 노드 번호
    edges[i]: i번 노드와 연결된 노드들의 리스트

    return: 방문한 노드들을 담은 set 반환
    '''
    q = deque([start])
    visited = set()
    while q:
        now = q.popleft()
        for next_node in edges[now]:
            if next_node not in visited:
                visited.add(next_node)
                q.append(next_node)
    return visited

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])

    return parent[x]

# 사실을 아는 사람과 Union시, 해당 사람이 부모노드가 되도록
def union(parent, a, b, know_truth):
    a = find(parent, a)
    b = find(parent, b)

    if a in know_truth and b in know_truth:
        return

    if a in know_truth:
        parent[b] = a
    
    elif b in know_truth:
        parent[a] = b
    
    else:
        if a < b:
            parent[b] = a
        
        else:
            parent[a] = b

n, m = map(int, input().split())
know_truth = list(map(int, input().split()))[1:]

parties = []
parent = list(range(n+1))

for _ in range(m):
    party_info = list(map(int, input().split()))
    party_len = party_info[0]
    party = party_info[1:]
    
    for i in range(party_len - 1):
        union(parent, party[i], party[i+1], know_truth)
    
    parties.append(party)
    
ans = 0
for party in parties:
    for i in range(len(party)):
        if find(parent, party[i]) in know_truth:
            break
    
    else:
        ans += 1

print(ans)