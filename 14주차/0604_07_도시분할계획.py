import sys
import heapq as h

input = sys.stdin.readline

# 0. get input

V, E = map(int, input().split())
dic = {}  # start : (end, weight)

# 1. make a dict

for _ in range(E):  # edge의 개수만큼
    start, end, weight = map(int, input().split())
    if start not in dic.keys():
        dic[start] = []
    if end not in dic.keys():
        dic[end] = []

    dic[start].append((weight, end))
    dic[end].append((weight, start))

# 2. initialization

start_node = 1
next_node = start_node

candidates = []
h.heapify(candidates)

visited = [False] * (V + 1)
visited[start_node] = True

cnt = 1
result = 0
longest = 0

# 3. Prim Algorithm

while cnt < V:

    for value in dic[next_node]:
        h.heappush(candidates, value)  # {key : from,  value : (weight, to)}

    while True:  # 가능한 최소 노드를 찾는 작업
        temp = h.heappop(candidates)
        to = temp[1]
        if visited[to] == False:  # 가능한 최소 노드를 찾았다면
            visited[to] = True  # 방문했으며
            weight = temp[0]
            result += weight  # 길을 업데이트 해주고
            if weight > longest:  # 가장 긴 길 업데이트
                longest = weight
            cnt += 1
            next_node = to
            break

print(result - longest)