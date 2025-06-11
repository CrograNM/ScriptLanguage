"""
    TUK - 목재총량

    접두사 합(PrefixSum):배열의 맨 앞부터 특정 위치 까지의 합을 미리 구해 놓은 것
"""
"""
    2차원 배열로 '숲'이 주어짐. 각 (i, j) 항목은 i번째 행의 j번째 나무의 양. (i, j 는 1부터 시작)
    산림청에서 지정한 범위의 목재 총량을 계산하라
"""

# 입력 받기
M, N = map(int, input().split())
forest = [list(map(int, input().split())) for _ in range(M)]

# 누적 합 배열 생성
S = [[0] * (N + 1) for _ in range(M + 1)]
print(S)

# 누적 합 계산
for i in range(1, M + 1):
    for j in range(1, N + 1):
        S[i][j] = S[i-1][j] + S[i][j-1] - S[i-1][j-1] + forest[i-1][j-1]
print(S)

# 쿼리 처리
C = int(input())
result = []
for _ in range(C):
    r1, c1, r2, c2 = map(int, input().split())
    total_wood = S[r2][c2] - S[r1-1][c2] - S[r2][c1-1] + S[r1-1][c1-1]
    result.append(str(total_wood))

# 결과 출력
print("\n".join(result) + "\n")
