""" 백준 13416 : 주식투자 """
"""
    입력 : 
        T개의 테스트 케이스 개수
            각 테스트 케이스의 첫째 줄 : N, 주식 데이터의 일수(day) 
            다음 N개의 줄에 A,B,C 세 회사의 일별 수익을 입력받는다.
"""

T = int(input())

for _ in range(T):
    N = int(input())
    money = 0
    for i in range(N):
        A,B,C = map(int, input().split())
        list = [A,B,C]
        list.sort()
        if (0 < list[-1]):
            money += list[-1]
    print(money)
    pass
