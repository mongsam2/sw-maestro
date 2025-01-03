# https://www.acmicpc.net/problem/14503

n, m = map(int, input().split())
r, w, d = map(int, input().split())

# 0 1 2 3  :  북 동 남 서
board = []
for _ in range(n): # 0이면 청소되지 않음, 1이면 벽, 2이면 청소 됨됨
    board.append(list(map(int, input().split())))

answer = 0 # 로봇이 청소한 칸의 개수

'''
def action(board, r, w, d):
    현재 상황에서 알고리즘을 한 번 수행
    board는 직접 참조
    return: is_working, nr, nw, d
'''
dr = [-1, 0, 1, 0]
dw = [0, 1, 0, -1]
def action(r, w, d):
    global answer, board

    if board[r][w] == 0:
        board[r][w] = 2
        answer += 1
    
    is_clean_around = True
    for direction in range(4):
        nr, nw = r+dr[direction], w+dw[direction]
        if board[nr][nw] == 0: # 근처 블록이 청소되지 않음
            is_clean_around = False
            break
    
    if is_clean_around:
        reverse = (d+2)%4
        nr, nw = r+dr[reverse], w+dw[reverse]
        if board[nr][nw] == 1: # 뒤가 벽이라면 작동을 멈춤
            return (False, r, w, d)
        return (True, nr, nw, d)
    
    else:
        d = (d-1)%4
        nr, nw = r+dr[d], w+dw[d]
        if board[nr][nw] == 0:
            return (True, nr, nw, d)
        else:
            return (True, r, w, d)
        
is_working = True
while is_working:
    is_working, r, w, d = action(r, w, d)

print(answer)