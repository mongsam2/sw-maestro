# https://www.acmicpc.net/problem/13458
from math import ceil

n = int(input())
lst = list(map(int, input().split()))
b, c = map(int, input().split())

total = len(lst)
cache = dict()
for num in lst:
    if num in cache:
        total += cache[num]
        continue

    count = 0 # 부 감독의 수
    remain = num - b # 총 감독이 볼 수 없는 학생 수

    if remain <= 0:
        count = 0
    else:
        count = ceil(remain/c)
    
    total += count

    if num not in cache:
        cache[num] = count
        
print(total)
