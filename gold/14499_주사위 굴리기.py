# https://www.acmicpc.net/problem/14499

n, m, x, y, k = map(int, input().split())
board = []
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

for _ in range(n):
    board.append(list(map(int, input().split())))
order = list(map(int, input().split()))

def next_dice(direct:int, dice:list):
    _, one, two, three, four, five, six = dice

    if direct == 1:
        dice[1], dice[3], dice[6], dice[4] = four, one, three, six
    
    elif direct == 2: 
        dice[4], dice[1], dice[3], dice[6] = one, three, six, four
    
    elif direct == 3:
        dice[2], dice[1], dice[5], dice[6] = one, five, six, two

    else:
        dice[2], dice[1], dice[5], dice[6] = six, two, one, five


location = [x, y]
dice = [0 for _ in range(7)] # 1, 2, 3, 4, 5, 6
for direct in order:
    new_x = location[0] + dx[direct]
    new_y = location[1] + dy[direct]
    if (new_x < 0 or new_x >= n) or (new_y < 0 or new_y >= m):
        continue

    location[0] = new_x
    location[1] = new_y
    next_dice(direct, dice)
    board_number = board[location[0]][location[1]]

    if board_number == 0:
        board[location[0]][location[1]] = dice[6]
    else:
        dice[6] = board_number
        board[location[0]][location[1]] = 0
    print(dice[1])
