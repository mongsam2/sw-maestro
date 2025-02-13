# https://www.acmicpc.net/problem/11725

from collections import deque

n = int(input())
tree = {node:[] for node in range(1, n+1)}
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs():
    answer = {i: 0 for i in range(1, n+1)}
    q = deque([1]) # node, parent
    visited = [False for _ in range(n+1)]
    visited[1] = True
    while q:
        current = q.popleft()
        for next_node in tree[current]:
            if not visited[next_node]:
                answer[next_node] = current
                visited[next_node] = True
                q.append(next_node)
    return answer

answer = bfs()
for i in range(2, n+1):
    print(answer[i])

'''from collections import deque
import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
tree = {i: [] for i in range(1, n+1)}
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [-1 for _ in range(n+1)]
def bfs():
    q = deque([1])
    visited = [False for _ in range(n+1)]
    visited[1] = True
    while q:
        current = q.popleft()
        for next_node in tree[current]:
            if not visited[next_node]:
                parent[next_node] = current
                visited[next_node] = True
                q.append(next_node)
bfs()
for i in range(2, n+1):
    write(str(parent[i]))
    write("\n")'''