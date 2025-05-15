"""
    보드 게임 최대 점수
"""
"""
    말을 상하좌우 이동 가능, 이동 칸에 쓰여진 점수 획득
    
"""
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
k = int(input())
#copy = board[:]

def DP(copy):
    dp = [[[0]*m for _ in range(n)] for _ in range(k+1)]
    #print(dp)
    #print(board)
    #print(board)
    for i in range(n):
        for j in range(m):
            dp[0][i][j] = 0
    #print("-------------------")
    #print(board)
    """
        dp[t][i][j] = max(dp[t-1][i-1][j], dp[t-1][i+1][j], dp[t-1][i][j-1], dp[t-1][i][j+1]) 
                        + board[i][j]   # 단, 이동한 위치가 보드 범위를 벗어나면 무시합니다
    """
    for t in range(1, k+1):
        for i in range(n):
            for j in range(m):
                max_list = []
                if i-1 >= 0:
                    max_list.append(dp[t - 1][i - 1][j])
                if j-1 >= 0:
                    max_list.append(dp[t - 1][i][j - 1])
                if i+1 < n:
                    max_list.append(dp[t - 1][i + 1][j])
                if j+1 < m:
                    max_list.append(dp[t - 1][i][j + 1])
                # print(max_list)
                # print("보드=========",board[i][j])
                dp[t][i][j] = max( max_list ) + board[i][j]
        # print(dp[t])
    # find max
    max_result = -1
    for i in range(n):
        for j in range(m):
            if max_result < dp[k][i][j]:
                max_result = dp[k][i][j]

    print(max_result)

DP(board[:])