# https://www.acmicpc.net/problem/1932

'''
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

dp
dp[i][j]: i층 j번째 블록까지 왔을 때의 최대값

j==0, j==i일 때만 특수하게 처리리

먼저 j-1이 0 이상인지 확인
j==i인지 확인 (위 층에 확인할 수가 존재하지 않는다.)
dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
'''

n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp = [[0 for j in range(i+1)] for i in range(n)]
dp[0][0] = triangle[0][0]

for i in range(1, n):
    for j in range(i+1):

        if j == 0:
            dp[i][j] = triangle[i][j] + dp[i-1][j]
        
        elif i == j:
            dp[i][j] = triangle[i][j] + dp[i-1][j-1]

        else:
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])

answer = max(dp[n-1])
print(answer)