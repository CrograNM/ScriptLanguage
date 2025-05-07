"""병사 배치하기"""
"""
    < 다이나믹 복습 >
    다이나믹 프로그래밍은 점화식으로 표현할 수 있다면 다이나믹 프로그래밍
    점화식 표현? -> 인접한 항들의 관계식으로 표현할 수 있다면, 다이나믹 프로그래밍
    점화식을 만들기 위해 각 항의 정의를 만들자
"""
"""
    전형적인(알아야 하는) longest increasing Sub_Sequence
    
    모든 [ 0<=j<i ]에 대해
    D[i] = max(D[i], D[j]+1) if array[j] < array[i]
"""

n = int(input())
array = list(map(int, input().split()))

# 순서를 뒤집어 'LIS' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
# dp[i] : array[i]를 끝 원소로 갖는 LIS 길이
# dp[i] = max( dp[i], dp[j]+1 ), if array[j] < array[i] (0<=j<i)
dp = [1]*n

# LIS 알고리즘 수행
for i in range(1, n):       # i = 1,2,...,n-1
    for j in range(0, i):   # j = 0,1,...,i-1
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

"""
    입력
7
15 11 4 8 5 2 4
"""
# 열외 해야 하는 병사의 최소 수 출력
print(dp)
print(n - max(dp))  # 2
