# 다시풀기 - 스택과 곱셈의 분배법칙을 이용한 문제
# 골드5

bracket = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):

    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    elif bracket[i] == "]":
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)