"""
    강연 중복 가능 (복수 예약 허용, 취소시 패널티 존재)

    하루에 한 개만 수행 가능하지만, 여러 강연이 같은 날에 예약되어 있을 수 있다.
    겹칠 경우 가장 수익이 낮은 것부터 취소되고, 취소된 pay의 절반이 벌금으로 차감
    최종 수익을 최대화하라
"""

import heapq

# 입력
n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]

# day 기준 오름차순 정렬
lectures.sort(key=lambda x: x[1])

pq = []          # 수익 낮은 순 저장
penalty = 0      # 벌금 합계

for pay, day in lectures:
    heapq.heappush(pq, pay)
    # 하루에 한 개만 가능, 현재까지 예약된 강연 수가 day를 초과하면
    if len(pq) > day:
        removed = heapq.heappop(pq)
        penalty += removed // 2  # 벌금은 절반만큼

# 수익 합에서 벌금을 뺀다
total_income = sum(pq)
final_income = total_income - penalty

print(final_income)
