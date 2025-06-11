
"""
    백준 1647 - 두개의 마을로 나누기

    최소 신장 트리를 만들되, 가장 큰 간선 하나는 끊어서 마을을 두 개로 만든다.
"""

# 최소 신장 트리를 만든 뒤, 가장 비용이 큰 간선을 끊어서 두 마을로 나누는 문제
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

# 간선을 비용 기준으로 오름차순 정렬
edges.sort(key=lambda x: x[2])

# 부모 테이블 초기화
parent = [i for i in range(n + 1)]
result = 0
max_cost = 0

for a, b, cost in edges:
    # 사이클이 생기지 않으면 연결
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost
        max_cost = cost  # 연결한 간선 중 가장 비용이 큰 것 기록

# 가장 비싼 간선을 끊어 두 마을로 나눈다
print(result - max_cost)
