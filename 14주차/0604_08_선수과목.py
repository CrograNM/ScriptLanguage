"""
    백준 14567 선수과목
"""

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
indegree = [0] * (N+1) # 진입차수를 0으로 초기화
graph = [[] for i in range(N+1)] # 연결 리스트 초기화

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # a에다가 b를 넣어준다.
    #1 2를 입력받으면 1번 노드에 연결된 간선인 2번 노드가 graph[1]에 저장된다.
    indegree[b] += 1 # 진입 차수를 추가해준다.

answer = [1] * (N+1) # 정답이 입력될 리스트

def topology_sort(): # 위상정렬 구현
    result = [] # 이 값은 위상 정렬 된 리스트
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0: # 진입차수가 0이면 큐에다 저장
            q.append(i)
            answer[i] = 1

    for i in range(1, N+1):
        now = q.popleft() # 선입선출
        result.append(now)

        for next in graph[now]:
            indegree[next] -= 1 # 진입 차수를 하나 빼준다.
            if indegree[next] == 0: # 진입차수가 0이 되면 큐에다 저장
                q.append(next)
            answer[next] = answer[now] + 1

    print(*answer[1:])
topology_sort()