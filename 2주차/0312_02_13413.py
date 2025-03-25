"""
    오셀로 재배치 다시해보기
    input = T, T*(초기상태, 목표상태)
    output = 목표상태로 가는 최소 횟수

    최소 횟수 저장
    -> 서로 다른 입력이 있다면 해당 인덱스의 WB 상태를 저장
        위치를 바꾸는 상황과, 색만 바꾸면 되는 상황들은
        저장된 서로 다른 WB 리스트의 W,B 중의 최대 개수와 같음.
        -> W 하나만 저장? -> 색을 바꿈 (1)
        -> W B 두개가 저장? -> 위치를 바꿈 (1)
        -> W B B 세개가 저장?
            -> B 하나는 위치 바꿈으로 카운트, 나머지 B 하나는 색 바꿈으로 카운트
"""

T = int(input())
for _ in range(T):
    N = int(input())
    before = input()
    after = input()

    list = []
    for i in range(N):
        if before[i] != after[i]:
            list.append(before[i])
    print(max(list.count('W'), list.count('B')))




