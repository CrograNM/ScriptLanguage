"""
    금광

    n * m 크기의 금광에 숫자가 있음

    0열에서 시작 (행은 자유), 우측 열로 이동
    오른쪽 위, 오른쪽 정면, 오른쪽 아래 세가지 경로 중 하나의 위치만 선택
    채굴자가 획득 가능한 최대 금의 크기
"""
"""
    dp[i][j] : 해당 칸에서 획득 가능한 최대 금의 크기
    
    dp[i][j] = gold_mine[i][j] + max( dp[i-1][j-1], dp[i][j-1], dp[i+1][j-1] ) 
    i, j가 인덱스 범위를 나가지 않도록 주의
"""

T = int(input())
"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""
def TEST():
    n, m = map(int, input().split())
    # 초기화
    input_list = list(map(int, input().split()))
    gold_mine = [[0] * m for _ in range(n)]

    i, j = 0, 0
    for inp in input_list:
        gold_mine[i][j] = inp
        j += 1
        if j % m ==  0:
            i += 1
            j = 0

    # DP 계산
    dp = [] + gold_mine
    for j in range(1, m):
        for i in range(n):
            dp_list = [dp[i][j - 1]]
            if i - 1 >= 0:
                dp_list.append(dp[i - 1][j - 1])
            if i + 1 < n:
                dp_list.append(dp[i + 1][j - 1])
            dp[i][j] = gold_mine[i][j] + max(dp_list)

    maximum = -1
    for i in range(n):
        if maximum < dp[i][m - 1]:
            maximum = dp[i][m - 1]
    print(maximum)

for _ in range(T):
    TEST()