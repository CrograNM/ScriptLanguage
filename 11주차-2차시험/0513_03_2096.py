"""
    백준 2096 - 내려가기
"""
"""
    DP? - 각 항에 대한 점화식을 만들자
    1 2 3
    1번 자리에서 아래로 내려갈 때, 3번으로 이동 불가
    2번 자리에서 아래로 내려갈 때, 모두 이동 가능
    3번 자리에서 아래로 내려갈 때, 1번으로 이동 불가
"""
"""
    dp[i][j] = i레벨 j번째 항까지의 최대값
    
    dp[i][j] = array[i][j] + max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) 
        if j = 0 : [i-1][0], [i-1][1] 만 max에 포함
        if j = 1 : max에 세개 모두 가능
        if j = 2 : [i-1][1], [i-1][2] 만 max에 포함
"""

N = int(input())
array = list()
for i in range(N):
    array.append(list(map(int, input().split())))

dp = [[0]*3 for _ in range(N)]
#print(dp)

# max 구하기
for i in range(N):
    for j in range(3):
        if i > 0:
            max_list = list()
            if j == 0:
                max_list.append(dp[i - 1][0])
                max_list.append(dp[i - 1][1])
            elif j == 1:
                max_list.append(dp[i - 1][0])
                max_list.append(dp[i - 1][1])
                max_list.append(dp[i - 1][2])
            elif j == 2:
                max_list.append(dp[i - 1][1])
                max_list.append(dp[i - 1][2])
            dp[i][j] = array[i][j] + max(max_list)
        else:
            dp[i][j] = array[i][j]
MAX = max(dp[N-1])

# min 구하기
for i in range(N):
    for j in range(3):
        if i > 0:
            min_list = list()
            if j == 0:
                min_list.append(dp[i - 1][0])
                min_list.append(dp[i - 1][1])
            elif j == 1:
                min_list.append(dp[i - 1][0])
                min_list.append(dp[i - 1][1])
                min_list.append(dp[i - 1][2])
            elif j == 2:
                min_list.append(dp[i - 1][1])
                min_list.append(dp[i - 1][2])
            dp[i][j] = array[i][j] + min(min_list)
        else:
            dp[i][j] = array[i][j]
MIN = min(dp[N-1])

print(MAX, MIN)

