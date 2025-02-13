# https://www.acmicpc.net/problem/15650

from itertools import combinations
import sys
write = sys.stdout.write

n, m = map(int, input().split())
lst = [i for i in range(1, n+1)]

comb = list(combinations(lst, m))
for nums in comb:
    print(*nums)
    