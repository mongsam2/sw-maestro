'''
- 오는 사람이 적은 파티부터 정렬

** 진실을 알고있는 사람이 있으면, 그 파티의 모든 사람은 진실 리스트에 포함! -> bfs 방식으로 추가

- 진실을 알고 있는 사람이 없으면, 과장해서 말하기 -> 과장된 사실 리스트에 사람들 추가
- 그렇지 않으면 진실을 말하기 -> 진실 리스트에 사람들 추가

** 과장만 듣거나, 진실만 듣는 것도 가능
'''
from collections import deque

answer = 0
n, m = map(int, input().split())
know = list(map(int, input().split()))
true_count, true_people = know[0], set(know[1:])
false_people = set()

party_list = []

graph = {i+1: set() for i in range(n)} # 그래프
for i in range(m):
    come = list(map(int, input().split()))
    come_count, come_people = come[0], come[1:]
    party_list.append((come_count, come_people))

    for come_person in come_people:
        graph[come_person].update(come_people)
party_list.sort()

for start in list(true_people):
    q = deque([start])
    while q:
        now = q.popleft()
        for next_node in graph[now]:
            if next_node not in true_people:
                true_people.add(next_node)
                q.append(next_node)
#print(true_people)



for come_count, come_people in party_list:
    say_lie = True
    for come_person in come_people:
        if come_person in true_people:
            say_lie = False
            break
    
    if say_lie:
        answer += 1
        false_people.update(come_people)
    
    else:
        true_people.update(come_people)

print(answer)