"""
    백준 1260 - DFS 와 BFS

    입력 :
    첫째줄에 정점개수 N, 간선개수 M, 시작 정점 번호 V가 주어진다.
    다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. (주어지는 간선은 양방향이다)

    출력 :
    첫째 줄에 DFS를 수행한 결과,
    둘째 줄에 BFS를 수행한 결과 출력

    1 2 4 3
    1 2 3 4 (띄어쓰기 있음)
"""
from collections import deque

N, M, V = map(int, input().split())

# 그래프를 Matrix 방식으로 받아온다.
graph = [[0]*(N+1) for _ in range(N+1)]

# M번의 반복으로 배열의 정점을 나타내는 칸들을 수정한다. 
# graph[i][j] = 1이면 [i+1]번, [j+1]번의 정점들은 서로 연결 되어있다는 뜻이다. 
# (양방향이므로 graph[j][i]도 수정해준다.)
for _ in range(M):
    i, j = map(int, input().split())
    graph[i][j] = 1  # 인덱스는 0부터 이므로 -1 하여 저장.  1번 정점 -> 0번 인덱스
    graph[j][i] = 1

visited_DFS = [0]*(N+1)
visited_BFS = visited_DFS.copy()

def dfs_rec(v):
    visited_DFS[v] = 1 #방문처리
    print(v, end=' ')
    for i in range(1, N+1):
        if graph[v][i] == 1 and visited_DFS[i] == 0:
            # 미 방문일 경우에 dfs 재귀 발동
            dfs_rec(i)

def dfs_stack(v): # LIFO
    stack = deque([v])
    while stack:            # 스택이 빌 때까지
        v = stack.pop()     # 스택의 제일 뒤의 값을 꺼낸다
        if visited_DFS[v] == 0:
            print(v, end=' ')
            visited_DFS[v] = 1

        # 방문할 수 있는 정점이 여러개인 경우에는 정점 번호가 작은 것을 먼저 방문
        # -> 스택은 거꾸로 나오니까 큰 것부터 검사해서 집어넣기
        for i in range(N, 0, -1): # i = N, N-1, ..., 1
            if visited_DFS[i] == 0 and graph[v][i]: # i번 정점을 방문하지 않았고 정점 v와 연결되어 있으면
                stack.append(i)                     # stack 뒤에 정점 i 추가


def bfs(v): # BFS = 큐로 구현
    queue = deque([v])
    while queue:
        v = queue.popleft() # deque의 첫번째 값을 꺼낸다.
        if visited_BFS[v] == 0:
            print(v, end=' ')
            visited_BFS[v] = 1

        for i in range(1, N+1): # i = 1, 2, 3,..., N
            if visited_BFS[i] == 0 and graph[v][i]: # i번 정점을 방문하지 않았고 정점 v와 연결되어 있으면
                queue.append(i)                     # queue 뒤에 정점 i 추가


#dfs_rec(V)
dfs_stack(V)
print()
bfs(V)