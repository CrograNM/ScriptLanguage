
"""
    새로운 길 만들기 (가중치 조건 02_MST + 임의 비용 변경)

    N개의 섬이 있고 M개의 다리가 있다.

    다리는 이미 몇 개 존재하고, 나머지를 연결하려면 새로운 다리를 설치해야 한다.
    단, 기존 다리는 비용이 0이고, 새로 설치하는 다리는 가중치가 주어진다.
    전체 섬을 연결하는 최소 비용을 구하라.
"""

# 기존 연결은 비용 0으로 간주하는 변형 02_MST 문제
def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, a, b):
    a = find(p, a)
    b = find(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

n, m, k = map(int, input().split())  # n개 섬, 기존 다리 m개, 후보 다리 k개

edges = []

# 기존 다리는 비용 0으로 추가
for _ in range(m):
    a, b = map(int, input().split())
    edges.append((0, a, b))

# 새로 설치할 수 있는 다리 목록
for _ in range(k):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
parent = [i for i in range(n + 1)]

result = 0
for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)
