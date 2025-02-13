# https://www.acmicpc.net/problem/15654

from itertools import permutations
import sys

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

perm = permutations(lst, m)

for nums in perm:
    print(*nums)