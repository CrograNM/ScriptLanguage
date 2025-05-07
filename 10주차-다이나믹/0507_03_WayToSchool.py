"""
    프로그래머스 - 등굣길
"""

def solution(m, n, puddles):
    # nxm 행렬
    # DP 테이블 사용.
    # 점화식, dp[i][j] = 여기까지 오는 최단 경로의 수
    # dp[i][0] = 1, dp[0][j] = 1, dp[1][1] = 0
    # dp[i][j] = dp[i-1][j] + dp[i][j-1] if not puddles

    # 일단 n*m으로 하고, 나중에 dp[m][n]을 출력
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        dp[i][1] = 1
    for j in range(1, m+1):
        dp[1][j] = 1
    for p in puddles:
        # p = [2,2] 같은 리스트임
        # p[0], p[1]을 통해 물 웅덩이의 좌표를 구함
        dp[p[1]][p[0]] = -1

    for i in range(2, n+1):
        for j in range(2, m+1):
            if dp[i][j] != -1:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    answer = dp[n][m] % 1000000007
    for i in range(0, n + 1):
        print(dp[i])
    return answer

print(solution(4, 3, [[2,2]]))