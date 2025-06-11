"""
    백준 2109 순회강연
"""

import sys
import heapq

def input() :
    return sys.stdin. readline() . rstrip()

n = int (input())

infoList = [list(map(int, input().split(" "))) for _ in range(n)]

#날짜 순으로 정렬
infoList.sort(key=lambda x : x[1])

pq=[]

for pay, day in infoList:
    heapq.heappush(pq, pay)
    # 강연일 보다 더 크다면 가장 작은값 제거
    if day < len(pq):
        heapq.heappop(pq)

print(sum(pq))