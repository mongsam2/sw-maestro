# https://www.acmicpc.net/problem/3190
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
k = int(input())
board = [[0 for j in range(n+1)] for i in range(n+1)] # 0: 아무것도 없음, 1: 사과, 2: 뱀
for _ in range(k):
    h, w = map(int, input().split())
    board[h][w] = 1

# L: 왼쪽 90도 회전 / D: 오른쪽으로 90도 회전 / 오: 0, 아: 1, 왼: 2, 위: 3
# 뱀을 연결 리스트로 표현
time_list = []
l = int(input())
for _ in range(l):
    info = input().split()
    x, c = int(info[0]), info[1]
    time_list.append((x, c))
time_list.append((10000, "L"))

# 뱀의 정보를 연결 리스트말고 큐로 나타내는 것이 더 간단
head = (1, 1)
snake =  deque([head]) # {꼬리: (다음 꼬리가 될 좌표)}
direction = 0
dh = [0, 1, 0, -1]
dw = [1, 0, -1, 0]
time = 0
for next_time, change in time_list: # 한 칸씩 이동
    interval = next_time - time

    for _ in range(1, interval+1): # 사과가 경로에 몇 개 있는지 확인
        new_h, new_w = head[0] + dh[direction], head[1] + dw[direction]
        time += 1

        if (new_h > n or new_h <= 0) or (new_w > n or new_w <= 0):
            #print(f"보드 벗어남: {new_h}, {new_w}")
            break

        if board[new_h][new_w] == 2:
            #print("자신의 몸을 밟음")
            break

        if board[new_h][new_w] == 0: # 사과가 없을 때, 꼬리 축소 
             #print("없음...")
             tail_h, tail_w = snake.popleft()
             board[tail_h][tail_w] = 0
            
        # 뱀의 head를 늘림
        board[new_h][new_w] = 2
        head = (new_h, new_w)
        snake.append(head)

    else: # 반복문이 정상적으로 끝났다면, 다음 time_list 확인
        if change == "L":
            direction -= 1
        else:
            direction += 1
        direction %= 4
        continue

    break
        
print(time)