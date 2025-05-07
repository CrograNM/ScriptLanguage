"""
    프로그래머스 - 등굣길
"""

def solution(m, n, puddles):
    dp = [[0]*(m) for _ in range(n)]
    puddleList = [[0]*m for _ in range(n)]
    for [c,r] in puddles:
        puddleList[r-1][c-1] = 1

    dp[0][0] = 1

    for r in range(n):
        for c in range(m):
            if puddleList[r][c] == 1:
                dp[r][c] = 0
            else:
                if r > 0:
                    dp[r][c] = dp[r-1][c]
                if c > 0:
                    dp[r][c] += dp[r][c-1]
    # 출력
    for i in range(n):
        print(dp[i])
    answer = dp[n-1][m-1] % 1000000007
    return answer

print(solution(4, 3, [[2,2]]))