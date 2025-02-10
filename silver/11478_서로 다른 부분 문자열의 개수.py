# https://www.acmicpc.net/problem/11478

'''s = input()
comb = set()

for i in range(len(s)):
    for j in range(i, len(s)):
        num = s[i:j+1]
        comb.add(num)
print(len(comb))'''

# 5 4 3 2 1
s = input()
answer = set()
for size in range(1, len(s)+1):
    for start in range(len(s)):
        sub_string = s[start:start+size]
        answer.add(sub_string)
print(len(answer))