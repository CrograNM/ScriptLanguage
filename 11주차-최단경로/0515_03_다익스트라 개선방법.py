import sys
input = sys.stdin.readline
import heapq
"""
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
"""
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())

# 노드 연결 정보 graph
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블 
distance = [INF]*(n+1)  
# 모든 간선 정보 입력
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []  # 최소 힙에 들어갈 리스트
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하고, 우선순위 큐에 삽입
    distance[start] = 0
    heapq.heappush(q,(0, start)) # (거리, 노드)의 쌍을 삽입
    while q:    # q가 빌 때까지 반복
        # 우선순위큐(최소 힙)에서 최단거리 노드 정보를 꺼낸다.
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있다면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 이웃 노드 확인
        for adjacent, weight in graph[now]:
            cost = dist + weight
            # 현재 노드를 거쳐서 이웃 노드를 가는 거리가 짧다면 갱신
            if cost < distance[adjacent]:
                distance[adjacent] = cost
                heapq.heappush(q, (cost, adjacent))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드 최단거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
