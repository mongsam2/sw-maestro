# https://www.acmicpc.net/problem/12789
from collections import deque
n = int(input())
line = deque(map(int, input().split()))
stack = []

last = 0
while last < n:
    if line and line[0] == last+1:
        last = line.popleft()
    elif stack and stack[-1] == last+1:
        last = stack.pop()
    elif line:
        stack.append(line.popleft())
    else:
        print("Sad")
        break
else:
    print("Nice")