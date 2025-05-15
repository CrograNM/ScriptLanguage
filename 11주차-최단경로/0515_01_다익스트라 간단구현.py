import sys
input = sys.stdin.readline

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

INF = int(1e9) #무한대값 (10억을 의미)
n, m = map(int, input().split()) # 노드, 간선 개수
start = int(input()) # 시작 노드

# 노드의 연결정보 2차원 그래프
graph = [[] for i in range(n+1)]

# 방문 처리 리스트
visited = [False]*(n+1)

# 최단거리 테이블, 무한대로 초기화
distance = [INF] * (n+1)

# 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

# print(graph)
#  [[],
#  [(2, 2), (3, 5), (4, 1)],    # 1번 노드에 연결된 (노드, 간선)
#  [(3, 3), (4, 2)],            # 2번
#  [(2, 3), (6, 5)],            # 3번
#  [(3, 3), (5, 1)],            # 4번
#  [(3, 1), (6, 2)],            # 5번
#  []]                          # 6번 노드는 연결된 노드가 없음

# 방문하지 않은 노드 중에서 가장 최단거리가 짧은 노드번호 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1): # 이 for문을 나중에 우선순위 큐로 대체할 수 있다.
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for (adjacent, weight) in graph[start]:
        distance[adjacent] = weight

    # 시작 노드를 제외한 n-1개 노드에 대해서 반복
    for i in range(n-1):
        # 현재 최단거리가 가장 짧은 노드를 꺼내서 방문처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for (adjacent, weight) in graph[now]:
            cost = distance[now] + weight
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[adjacent]:
                distance[adjacent] = cost
    pass
# 다익스트라 알고리즘 수행
dijkstra(start)
# 모든 노드로 가기 위한 최단거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])
        
# 다음은 우선순위 큐를 사용해 구현