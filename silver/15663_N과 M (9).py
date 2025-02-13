# https://www.acmicpc.net/problem/15663
from itertools import permutations

n, m = map(int, input().split())
lst = list(map(int, input().split()))

comb = permutations(lst, m)

for nums in sorted(set(comb)):
    print(*nums)