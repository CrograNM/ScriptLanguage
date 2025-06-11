"""
    구간 합 구하기 5 (백준 11660)
"""
"""
    2차원 배열에서 주어진 좌표 범위의 누적합을 빠르게 구하기
"""

# 2차원 누적합을 이용하여 직사각형 영역의 합을 O(1)에 구하는 문제

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * (n + 1)]
for _ in range(n):
    arr.append([0] + list(map(int, input().split())))

# 누적합 배열
sums = [[0] * (n + 1) for _ in range(n + 1)]

# 누적합 계산
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sums[i][j] = sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1] + arr[i][j]

# 쿼리 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = sums[x2][y2] - sums[x1 - 1][y2] - sums[x2][y1 - 1] + sums[x1 - 1][y1 - 1]
    print(result)