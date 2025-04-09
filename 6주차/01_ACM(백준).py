"""
    각 층에 W개의 방이 있는 H층 건물,
    손님은 101, 201, 301 순으로 채워진다.
"""

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split()) # H가 높이, N이 몇번째 손님인지
    """
            N 을 H로 나눈다 -> 나머지를 킵해야 함
            층수 : 10 % 6 -> 4
            방번호 : 10 // 6 + 1 -> 2 (101호 부터 시작하니까 1 더함)
                --> 402호
    """
    floor = N % H
    room = N // H + 1
    print( (floor*100) + room )
    pass
