"""
    TUK 0059 - Postfix 표현식
"""
"""
    ab+cd+e-a+- 
    
    스택을 활용해서 구현
    1. 문자가 연산자가 아니면 스택에 삽입
    2. 문자가 연산자가 아니면 스택에 삽입
    3. 연산자면 1,2를 pop, 괄호로 묶어 스택 삽입
"""

postfix = input()
stack = list()

for c in postfix:
    if c.isalpha():
        stack.append(c)
    elif c == '+' or c == '-':
        right = stack.pop()
        left = stack.pop()
        bundle = '(' + left + c + right + ')'
        stack.append(bundle)
        # print(stack)
print(stack.pop())