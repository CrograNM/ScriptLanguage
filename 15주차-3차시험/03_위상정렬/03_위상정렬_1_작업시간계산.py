"""
    03_위상정렬 :
        사이클이 없는 방향 그래프의 모든 노드를
        방향성에 거스르지 않도록 순서대로 나열하는 것.

    <작업시간계산 - 백준 2056>
    각 작업마다 걸리는 시간이 있고, 어떤 작업은 '선행 작업'이 끝나야 시작 가능하다. 전체 작업을 완료하는 최소 시간은?

"""

# 각 작업마다 걸리는 시간과 선행 작업이 있는 DAG에서
# 전체 작업 완료에 걸리는 최소 시간 구하기

from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
time = [0] * (n + 1)

# 입력 처리
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    time[i] = data[0]  # 현재 작업 시간
    for prereq in data[2:]:
        graph[prereq].append(i)
        indegree[i] += 1

# 작업을 마치는 데 걸리는 최대 시간 기록
result = time[:]
q = deque(i for i in range(1, n + 1) if indegree[i] == 0)

# 위상 정렬 + DP
while q:
    now = q.popleft()
    for nxt in graph[now]:
        result[nxt] = max(result[nxt], result[now] + time[nxt])
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

print(max(result))
