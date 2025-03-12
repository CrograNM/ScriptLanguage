
# 백준 문제집
# 파이썬 배우기 	automata
# IT기업 코테 유사 문제집    ses9928
# -> 연습하기(4학년 때 도움될듯)


# 사전 자료형 (dict, set) -> 해시테이블로 인해 시간 복잡도가 O(1)이다.

# 기본 input()은 살짝 느리다.
import sys
input = sys.stdin.readline
#A, B, C = map(int, input().split())
A, B, C = 10, 20, 30

# 포매팅
print(A, end=" ") # 개행금지
print(f"아아아{A}{B}{C}{C}")
print(f"와이거 {A:.3f}뭐야")
print(f"{A:@>5} 오 뭐임 {B:$>10}")

# in 연산자
print('k' in 'korea')
for c in 'korea':
    print(c, end=" ")
print()
L = [1, 2, 5, 10, 20]
for n in L:
    print(n, end=',')
print()

def abcd():
    pass # pass 키워드

for i in range(10): # i=0,1,2,3,4,5,6,7,8,9
    print(i, end=',')
print()