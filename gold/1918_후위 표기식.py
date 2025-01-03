# https://www.acmicpc.net/problem/1918

from collections import deque

s = input()

def pop_parentheses(stack):
    answer = deque([])
    while stack:
        c = stack.pop()
        if c == "(":
            break
        answer.appendleft(c)
    return list(answer) # 반환값 조심 
    # (하나의 문자열 형태로 반환한다면, 숫자 하나로 판단한다.)
    # (아직 연산하지 않은 부분이므로 함부로 합치면 안 된다.)

def select_calculate(expression:list, operator_list:list) -> list[str]:
    q = deque(expression)
    stack = []
    while q:
        current = q.popleft()
        if current in operator_list:
            num1 = stack.pop()
            num2 = q.popleft()
            stack.append(num1+num2+current)
        else:
            stack.append(current)
    return stack

# 재귀함수를 이용한 풀이
def calculate(s:str) -> str:
    '''
    input: 중위 표현식
    return:
        후위 표현식
    '''
    # 괄호가 있는 부분부터 계산
    stack = []
    for c in s:
        if c == ")":
            part = pop_parentheses(stack) # 괄호 안에 있는 부분만 추출
            stack.append(calculate(part)) # 괄호 안에 부분을 연산해서 스택에 추가

        else:
            stack.append(c)

    # 곱셈, 나눗셈을 먼저 체크해서 calculate
    stack = select_calculate(stack, ["*", "/"])

    # 덧셈, 뺄셈을 체크해서 calculate
    stack = select_calculate(stack, ["+", "-"])

    return "".join(stack)

answer = calculate(s)
print(answer)

