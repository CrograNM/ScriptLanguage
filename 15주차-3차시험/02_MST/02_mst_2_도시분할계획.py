
"""
    도시분할계획 (기본MST + 간선제거)

    N개의 집과 M개의 도로가 있다.
    모든 집들을 연결하되, 도로 유지비의 합이 최소가 되도록 연결해야 한다.
    단, 마을을 2개로 분할해야 하므로 MST를 만든 뒤, 가장 비용이 큰 간선 하나는 제거해야 한다.
"""

# MST를 만들고 가장 비싼 간선을 제거하는 방식
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

edges.sort(key=lambda x: x[2])  # 비용 기준 정렬
parent = [i for i in range(n + 1)]

total_cost = 0
max_cost = 0

for a, b, cost in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost
        max_cost = cost  # 가장 마지막 간선이 가장 비쌈

print(total_cost - max_cost)
