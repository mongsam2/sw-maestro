# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline

def get_prefix(n, board):
    answer = [[0 for j in range(n+1)] for i in range(n+1)]
    for i in range(1, n+1):
       for j in range(1, n+1):
          answer[i][j] = answer[i-1][j] + answer[i][j-1] + board[i][j] - answer[i-1][j-1]
    return answer

# y1-1, x2   y2, x1-1
def cal(prefix, h1, w1, h2, w2):
    return prefix[h2][w2] - prefix[h1-1][w2] - prefix[h2][w1-1] + prefix[h1-1][w1-1] 

n, m = map(int, input().split())
board = [[0 for _ in range(n)]]
for _ in range(n):
    board.append([0] + list(map(int, input().split())))

#print(board)
prefix = get_prefix(n, board)
#print(prefix)
for _ in range(m):
    h1, w1, h2, w2 = map(int, input().split())
    answer = cal(prefix, h1, w1, h2, w2)
    print(answer)



'''n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

cumulate = [[0]*(n+1) for _ in range(n+1)]
cumulate[1][1] = board[0][0]

for j in range(2, n+1):
    cumulate[1][j] = cumulate[1][j-1] + board[0][j-1]

for i in range(2, n+1):
    cumulate[i][1] = cumulate[i-1][1] + board[i-1][0]

for i in range(2, n+1):
    for j in range(2, n+1):
        cumulate[i][j] = cumulate[i][j-1] + cumulate[i-1][j] - cumulate[i-1][j-1] + board[i-1][j-1]

for k in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = cumulate[x2][y2] - cumulate[x2][y1-1] - cumulate[x1-1][y2] + cumulate[x1-1][y1-1]
    write(str(answer))
    write("\n")'''