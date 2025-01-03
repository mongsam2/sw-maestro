# https://www.acmicpc.net/problem/13460

from collections import deque

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(input()))

for i in range(1, n-1):
    for j in range(1, m-1):
        if board[i][j] == "R":
            red_idx = (i, j)
        elif board[i][j] == "B":
            blue_idx = (i, j)
        elif board[i][j] == "O":
            o_idx = (i, j)

# 상 좌 하 우
dh_list = [-1, 0, 1, 0]
dw_list = [0, -1, 0, 1]
def step(board, red_idx:tuple, blue_idx:tuple, direct:int):
    '''
    direct 방향으로 기울였을 때, 구슬들의 새로운 위치를 반환
    '''
    answer = []
    dh, dw = dh_list[direct], dw_list[direct]
    for i, j in [red_idx, blue_idx]:
        is_back = False # 경로에 다른 구슬이 있으면 한 칸 복귀해야 함
        while board[i+dh][j+dw] != "#": # 다음 칸이 벽이라면 이동 멈춤
            i += dh
            j += dw

            if (i, j) == red_idx or (i, j) == blue_idx:
                is_back = True

            elif board[i][j] == "O": # 구멍에 도달했으면 구멍 위치로 저장
                break

        else: # 공들이 구멍에 빠지지 않았을 때,
            if is_back:
                i -= dh
                j -= dw
        answer.append((i, j))

    return answer # [빨간색, 파란색]


q = deque([])
for direct in range(4):
    q.append([1, red_idx, blue_idx, direct]) # [기울인 횟수, 빨간색, 파란색, 방향]

while q:
    cnt, red, blue, direct = q.popleft()

    if cnt > 10: # 10번 안에 불가능할 때
        print(-1)
        break
    
    new_red, new_blue = step(board, red, blue, direct)
    if new_red == red and new_blue == blue: # 위치가 그대로일 때
        continue

    if board[new_red[0]][new_red[1]] == "O" and board[new_blue[0]][new_blue[1]] != "O":
        print(cnt)
        break

    elif board[new_blue[0]][new_blue[1]] == "O":
        continue

    for next_direct in range(4):
        if next_direct == (direct+2)%4: # 이전에 왔던 방향으로 되돌아가지 않도록
            continue
        q.append([cnt+1, new_red, new_blue, next_direct])

else:
    print(-1)