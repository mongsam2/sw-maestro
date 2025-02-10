# https://www.acmicpc.net/problem/9465
import sys
input = sys.stdin.readline

def f(lst, n):
    dp = [[0 for j in range(n)] for i in range(2)]
    dp[0][0], dp[1][0] = lst[0][0], lst[1][0]
    for j in range(1, n):
        dp[0][j] = max(lst[0][j] + dp[1][j-1], dp[0][j-1])
        dp[1][j] = max(lst[1][j] + dp[0][j-1], dp[1][j-1])
    return dp

t = int(input())
for _ in range(t):
    n = int(input())
    lst = []
    for i in range(2):
        lst.append(list(map(int, input().split())))
    dp = f(lst, n)
    print(max(dp[0][-1], dp[1][-1]))

'''t = int(input())
for _ in range(t):
    n = int(input())
    board = []
    dp = [[0]*n for line in range(2)]
    for i in range(2):
        board.append(list(map(int, input().split())))

    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    for col in range(1, n):
        for row in range(2):
            dp[row][col] = max(dp[(row+1)%2][col-1] + board[row][col], dp[row][col-1]) 
    print(max(dp[0][n-1], dp[1][n-1]))'''
    
'''
dp
dp[i][j] = max(dp[(i+1)%2][j-1] + board[i][j], dp[i][j-1])
'''