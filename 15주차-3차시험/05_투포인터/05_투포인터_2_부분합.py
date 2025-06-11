"""
    백준 1806 - 부분합
    합이 S 이상이 되는 '가장 짧은' 연속 부분 수열의 길이 구하기.
"""

# 길이가 N인 수열에서, 연속된 수들의 합이 S 이상이 되는
# 가장 짧은 부분 수열의 길이를 구하는 문제

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
total = 0
min_len = n + 1  # 존재하지 않는 경우 대비

for right in range(n):
    total += arr[right]
    # 조건을 만족할 때까지 왼쪽 포인터 이동
    while total >= s:
        min_len = min(min_len, right - left + 1)
        total -= arr[left]
        left += 1

# 불가능한 경우 0 출력
print(min_len if min_len != n + 1 else 0)