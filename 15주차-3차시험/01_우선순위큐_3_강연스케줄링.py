"""
    강연 스케줄링
    하루에 T시간 강연 가능

    N: 강연 개수
    T: 하루 최대 시간 (정수)
    pi: 수익
    di: 마감일 (day)
    ti: 소요 시간 (시간 단위)

    각 날짜마다 가능한 시간 안에서 강연을 스케줄해 총 수익을 최대로 하라
"""

"""
    입력:
        N T
        p1 d1 t1
        p2 d2 t2
        ...
        pN dN tN
"""

import heapq

n, max_time_per_day = map(int, input().split())
lectures = [tuple(map(int, input().split())) for _ in range(n)]

# 마감일이 빠른 순서로 정렬
lectures.sort(key=lambda x: x[1])

# 현재까지 고려한 강연들의 시간을 합치되, 가장 수익이 낮은 것부터 제거
pq = []  # (pay, duration)
total_time = 0

for pay, deadline, duration in lectures:
    total_time += duration
    heapq.heappush(pq, (pay, duration))

    # 현재까지의 총 시간 > 가능한 시간 (날짜 * 하루시간)
    if total_time > deadline * max_time_per_day:
        # 가장 수익 낮은 강연 제거
        min_pay, min_dur = heapq.heappop(pq)
        total_time -= min_dur

# 남은 강연들의 수익 합계
print(sum(pay for pay, _ in pq))

