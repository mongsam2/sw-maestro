# https://www.acmicpc.net/problem/14501

'''
dp
dp[i] = max(lst[i] + dp[i+d], dp[i+1]) i날의 상담을 하는 경우와 하지 않는 경우를 비교
'''

n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)] # [상담 소요 일, 수익]

dp = [0]*(n+1) # dp[n]은 임시로 선언
for day in range(n-1, -1, -1):
    if day + lst[day][0] > n: # 상담을 진행할 수 없는 경우
        dp[day] = dp[day+1]
    else:
        dp[day] = max(lst[day][1] + dp[day + lst[day][0]], dp[day+1])

print(dp[0])