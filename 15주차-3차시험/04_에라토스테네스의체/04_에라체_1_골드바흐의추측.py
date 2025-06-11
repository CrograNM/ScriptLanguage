"""
    에라토스테네스의 체 - 골드바흐
    주어진 짝수 n에 대해, 두 소수의 합으로 나타낼 수 있는 조합을 출력.
"""

# 주어진 짝수 n에 대해 두 소수의 합으로 나타낼 수 있는 경우 중
# 차이가 가장 작은 두 소수를 출력

MAX = 10000

# 소수 판별 배열
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

t = int(input())
for _ in range(t):
    n = int(input())
    # n/2부터 역순으로 탐색 → 차이가 가장 작은 조합을 찾기 위해
    for i in range(n // 2, 1, -1):
        if is_prime[i] and is_prime[n - i]:
            print(i, n - i)
            break