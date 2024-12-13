# https://www.acmicpc.net/problem/1629

a, b, c = map(int, input().split())

def power(a, b, c):
    if b == 0:
        return 1
    
    num = power(a, b//2, c)

    if b%2 == 0:
        return (num * num)%c
    else:
        return (num * num * a)%c
    
answer = power(a, b, c)
print(answer)