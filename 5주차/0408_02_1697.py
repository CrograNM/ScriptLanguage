"""
    백준 1697 : 숨바꼭질 (BFS)
"""
from collections import deque

"""
    수빈의 위치 N
    동생의 위치 K
    
    N이 K가 되는 최소 횟수 구하기
    
    N은 -1, +1, *2 중에 선택 가능
"""
N, K = map(int, input().split())

max_coord = 100000
visited = [0] * (max_coord + 1)     # '인덱스 좌표'에 도착한 '시간'을 저장한다.
                                    # [5]:0 -> [10]:1 -> [9]:2 -> [18]:3 -> [17]:4
                                    #                     [11]:2  
                                    #           [4]:1     [20]:2  
                                    #           [6]:1

q = deque([N])
while q:    # q가 비어있을 때까지 실행
    x = q.popleft()
    if x == K:
        print(visited[x])
        break
    
    for i in (x-1, x+1, 2*x):
        if 0 <= i <= max_coord and visited[i] == 0: # x의 다음 좌표가 범위 내면서 미방문일 경우
            visited[i] = visited[x] + 1             # 방문처리: 시간 등록
            q.append(i)                             # 큐에 방문한 좌표 등록
                                                    # 자동으로 앞에 있는 좌표들이 빠지면서 다음 좌표 검사를 위해 큐에 삽입하는 BFS 구조
    
    