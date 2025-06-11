"""
     순회강연인데, 하루에 K개 받기 가능
"""

import heapq

n, k = map(int, input().split())  # n개의 제안, 하루 최대 k개 선택

lectures = [tuple(map(int, input().split())) for _ in range(n)]
lectures.sort(key=lambda x: x[1])

pq = []
for pay, day in lectures:
    heapq.heappush(pq, pay)
    if len(pq) > day * k:  # 하루에 k개까지 가능
        heapq.heappop(pq)

print(sum(pq))
