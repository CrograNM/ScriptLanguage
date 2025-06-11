"""
    백준 2109 순회강연
"""
"""
    각 대학에서 d일안에 와서 강연을 하면 p의 비용을 지불하겠다 알림
    하루 최대 한곳에서 강연을 한다고 할 때, 가장 많은 돈을 벌 수 있도록 순회강연 한다
    
    첫째 줄에 정수 n, 다음 n개의 줄에는 각 대학에서 제시한 p(비용)값, d(기한)값이 주어짐
"""
"""
7
20 1
2 1
10 3
100 2
8 2
5 20
50 10

= 185
"""

import heapq

n = int (input())

infoList = [ list(map(int, input().split())) for _ in range(n) ]
#print(infoList)

#날짜 순으로 정렬 (정렬된 상태로 순회해야 일자가 중복 됬을 때가 검출될 거임)
infoList.sort(key=lambda x : x[1]) # [1] 인덱스 값이 d값임
print(infoList)

pq=[]

for pay, day in infoList:
    heapq.heappush(pq, pay) # pay값을 pq에 저장

    # pq에 저장된 강연 수가 제한된 강연일(day) 보다 더 크다면 pq 중 가장 작은값 제거
    if day < len(pq):
        heapq.heappop(pq)

print(sum(pq))