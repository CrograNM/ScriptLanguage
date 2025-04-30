"""
    컵홀더
    좌석 수 와, S, LL이 주어지며, 좌석 옆에 컵홀더 설치 가능,
    컵홀더를 사용할 수 있는 최대 사람 수를 출력
    LL은 항상 두개의 쌍이며, 컵홀더는 *LL* 식으로 배치된다.
"""
from collections import deque, Counter

"""
    입력 
    4
    SLLS
    
    출력 : ( *S*LL*S* 이므로 4명이 사용 가능 ) -> 4
"""
"""
    1. 일단 주어진 문자열을 가지고 새로운 문자열을 생성한다 SLLS -> *S*LL*S* 
    과정 : 두개의 문자열 배열이 있고, SLLS 를 순차적으로 탐색하며 
    S인 경우 -> *S를 삽입,
    LL인 경우 -> *LL을 삽입
    문자열 탐색이 끝나면 -> *를 삽입
"""

N = int(input())
list = input()
queue = deque(list)
#print(queue)

seats = ''
while True:
    if len(queue) == 0:
        seats += '*'
        break
    x = queue.popleft()
    if x == 'S':
        seats += '*S'
    elif x == 'L':
        seats += '*LL'
        queue.popleft()

# print(seats)
counter = Counter(seats)
if counter['*'] > N:
    print(N)
else :
    print(counter['*'])





