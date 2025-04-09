"""
    TUK 0045 중요한 교차로
"""

from collections import deque

# 스택 DFS (Last In First Out)
def DFS(v, i, graph, N, visited):
    stack = deque([v])  # 더 빠른 덱을 사용, [v]를 넣어서 초기화
    while stack:        # 스택이 빌 때까지
        v = stack.pop() # 스택 제일 뒤에서 꺼냄
        if not visited[v]:      # 방문하지 않았다면
            visited[v] = True   # 방문 처리
            for j in range(1, N+1): # j = 1,2,3,...,N
                # i가 아니고, 방문하지 않았고, V와 연결되었으며, 스택에도 없다면
                if j!=i and not visited[j] and graph[v][j] and not j in stack:
                    stack.append(j)
    pass

N, M = map(int, input().split())

graph = [[False]*(N+1) for _ in range(N+1)] # N*N 2차원 배열, graph[i][j] = True 라면 i<-->j
                # N+1 크기의 배열이므로, 인덱스 1은 무시한다
#print(graph)

# 도로 M 정보 입력
for _ in range(M):
    i, j = map(int, input().split())
    graph[i][j] = True
    graph[j][i] = True

answer = [] # 중요한 교차로의 목록

for i in range(1, N+1): # i = 1,2,3...N 모든 교차로에 대해서 중요한지 검사
    visited = [False]*(N+1) # 모든 교차로 unvisited 설정
    if i == 1:
        v = 2 # 임의의 교차로 설정
    else:
        v = 1 # 임의의 교차로 설정
    DFS(v, i, graph, N, visited) # BFS 여도 상관 없다. V에서 시작해서 완전 탐색 시도하기
    
    # i 를 제외하고 unvisited 교차로가 존재하면 i는 중요한 교차로
    for j in range(1, N+1):
        if j != i and not visited[j]:   # unvisited 교차로가 존재하면
            answer.append(i)            # i는 중요한 교차로
            break

print(len(answer))  # 중요한 교차로 개수
for j in answer:    # 한 줄에 하나씩 중요한 교차로를 오름차순으로 출력
    print(j)