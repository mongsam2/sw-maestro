# https://www.acmicpc.net/problem/14502

'''
최대 64칸
경우의 수: 64 * 63 * 62 / 3 * 2 * 1 = 41664가지의 수
bfs: 

방법1: 완전탐색 
'''
from collections import deque
from itertools import combinations
import sys
from typing import Iterable
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

blanks = [] # 빈칸의 인덱스를 담은 리스트
viruses = [] # 바이러스가 있는 위치
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            blanks.append((i, j))
        elif board[i][j] == 2:
            viruses.append((i, j))

def difuse(board, walls:Iterable, viruses:Iterable):
    '''
    새로 퍼진 바이러스의 개수를 반환
    '''
    visited = set()
    visited.update(viruses)
    visited.update(walls)

    add_virus = 0 # 새로 전염된 바이러스의 개수
    
    q = deque(viruses)
    dh = [0, 0, 1, -1]
    dw = [1, -1, 0, 0]

    while q:
        current = q.popleft()
        for i in range(4):
            nh, nw = current[0]+dh[i], current[1]+dw[i]
            if (0 <= nh < n) and (0 <= nw < m) and (nh, nw) not in visited and board[nh][nw] == 0:
                visited.add((nh, nw))
                add_virus += 1
                q.append((nh, nw))
    
    return add_virus


all_combination = combinations(blanks, 3)
answer = 0
for comb in all_combination:
    add_virus = difuse(board, comb, viruses)
    answer = max(answer, len(blanks) - add_virus)

print(answer - 3)