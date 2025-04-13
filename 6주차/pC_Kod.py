"""
    Kod
"""
"""
    입력
    
    첫째줄 : 참가자 수 N
    둘째줄 : N개의 정수 (회장 기준 참가자의 순위 : 이건 순위 순으로 정렬됨)
    셋째줄 : N개의 정수 (협회회원 투표 수 : 이건 참가번호 순으로 정렬됨)
    
    3
    1 2 3       -> '1':3,       '2':2,      '3':1
    50 10 20    -> '1':3+3,     '2':2+1,    '3':1+2
"""

N = int(input())
# dict 리스트를 만들자 [{1:점수}, {2:점수}, {3:점수}]
ranker = [[i, 0] for i in range(1, N+1)]
#print(ranker[0]) : (1,0)
#print(ranker[0][1]) : 0

r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))

r1_point = N
for x in r1:
    ranker[x - 1][1] += r1_point
    r1_point -= 1


r2_list = {x:0 for x in r2}
print(r2_list)

for i in range(1, N+1):
    r2_list[i-1] += i
print(r2_list)
