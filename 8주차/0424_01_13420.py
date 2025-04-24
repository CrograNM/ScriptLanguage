"""
    백준 13420 - 사칙연산
"""

"""
    사칙연산 기호는 1개만 사용
    수식은 문자와 기호가 공백으로 구분되어 주어진다.
    파이썬은 split에 넣은 기호를 기준으로 나눠준다
    파이썬은 문자열도 eval 함수를 통해 정수로 계산해준다.
"""
T = int(input())

for _ in range(T):
    left, right = input().split('=')
    if eval(left) == int(right) :
        print('correct')
    else:
        print('wrong answer')