"""
    최소 비용으로 2차원 맵 탈출하기
    다익스트라 + 01_우선순위큐

    N × N 크기의 맵이 있다. 각 칸에는 지나는 데 드는 비용이 들어 있다.
    (0, 0)에서 시작해서 (N-1, N-1)까지 이동하고자 한다.
    상하좌우로 이동할 수 있으며, 지나간 칸의 비용은 모두 누적된다.
    최소 비용으로 이동하는 경로를 찾고, 해당 비용을 출력하라.
"""
"""
    N
    맵의 각 줄에 N개의 정수 (0 이상 9 이하의 숫자, 비용이 2차원 맵으로 되어있음) 
    
    (0, 0)부터 (N-1, N-1)까지의 최소 비용을 출력
"""

import heapq

n = int(input())
graph = [ list(map(int, input().split())) for _ in range(n) ]

# 최소 비용을 저장하는 배열
dist = [[float('inf')] * n for _ in range(n)]
dist[0][0] = graph[0][0]

# 우선순위 큐: (누적비용, x, y)
pq = [(graph[0][0], 0, 0)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while pq:
    cost, x, y = heapq.heappop(pq)

    if dist[x][y] < cost:
        continue  # 이미 더 짧은 경로 존재

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            next_cost = cost + graph[nx][ny]
            if next_cost < dist[nx][ny]:
                dist[nx][ny] = next_cost
                heapq.heappush(pq, (next_cost, nx, ny))

print(dist[n-1][n-1])


