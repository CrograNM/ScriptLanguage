"""
    접두사 합(PrefixSum):
        배열의 맨 앞부터 특정 위치 까지의 합을 미리 구해 놓은 것
"""

n = 5
data =            [10, 20, 30,  40,  50]
# prefix_sum = [0, 10, 30, 60, 100, 150]

# 접두사 합(Prefix Sum) 배열 계산
sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

# 구간 합 계산(세 번째 수부터 네 번째 수 까지
left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left - 1])