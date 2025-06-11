
"""
    행성 터널 (백준 2887)
    좌표 기반 그래프 → 모든 간선 직접 생성,  행성 터널 (백준 2887)

    각 노드는 (x, y, z) 좌표를 가진 행성
    간선은 두 행성 간의 거리로 계산됨
    간선을 주지 않고 노드 좌표만 줌 → 직접 거리 계산 필요
    최단 거리 터널(최소 신장 트리)을 구축해야 함
"""

# 백준 2887 - 행성 터널
# 각 노드는 3차원 좌표를 가지며, 직접 모든 간선을 구성한 뒤 크루스칼 수행

import sys
input = sys.stdin.readline

def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]

def union(p, a, b):
    a, b = find(p, a), find(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b

n = int(input())
points = []

for i in range(n):
    x, y, z = map(int, input().split())
    points.append((i, x, y, z))  # (번호, x, y, z)

edges = []

# 축 별로 정렬 후 인접 행성 간의 거리만 간선으로 저장
for dim in range(1, 4):  # x, y, z 각각
    points.sort(key=lambda p: p[dim])
    for i in range(n - 1):
        a_id = points[i][0]
        b_id = points[i + 1][0]
        cost = abs(points[i][dim] - points[i + 1][dim])
        edges.append((cost, a_id, b_id))

# 크루스칼 시작
edges.sort()
parent = [i for i in range(n)]
res = 0

for cost, a, b in edges:
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        res += cost

print(res)
