"""
    백준 11055 - 가장 큰 증가 부분 수열
"""
"""
    수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것 구하기
"""

n = int(input())
array = list(map(int, input().split()))
#print(array)

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
# dp[i] = max( dp[i], dp[j] + array[i] ), if array[j] < array[i] (0<=j<i)
dp = array[:] # 깊은 복사
#print(dp)

# LIS 알고리즘 수행
for i in range(1, n):       # i = 1,2,...,n-1
    for j in range(0, i):   # j = 0,1,...,i-1
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + array[i])

print(max(dp))