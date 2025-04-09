"""
    프로그래머스 - 여행경로 (DFS)
"""
def solution(tickets): # [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    # step 1 : 티켓을 조회해서 중복되지 않는 공항 리스트를 알파벳 순서로 생성한다.
    ports = set() # 공항 집합
    for a, b in tickets:
        ports.add(a)
        ports.add(b)
    ports = list(ports) # list로 형변환
    ports.sort()        # 알파벳 오름차순 정렬
    # print(ports)

    # step 2 : 티켓 정보와 ports를 이용해서 graph[][] int형 2차원 배열을 구성하겠다
    N = len(ports)
    graph = [[0]*(N) for _ in range(N)]
    for a,b in tickets:
        i = ports.index(a)  # ports 리스트에서 a공항의 인덱스를 구한다
        j = ports.index(b)  # ports 리스트에서 b공항의 인덱스를 구한다
        graph[i][j] += 1    # 동일한 경로 티켓이 여러 장 있을 수 있다.

    # step 3 : ICN에서 시작해서 DFS로 모든 티켓을 소진하도록 탐색한다.
    nTickets = len(tickets) # 티켓의 개수 관리
    port = 'ICN'            # 시작 공항


    answer = []
    return answer



print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# ["ICN", "JFK", "HND", "IAD"]
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
# ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]