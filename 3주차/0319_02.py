"""
    1이 될 때까지
"""

n, k = map(int, input().split())
result = 0
while True:
    # n이 k로 나눠 떨어지는 수가 될때까지 1빼기
    target = (n//k)*k
    result += (n - target)
    n = target

    # n이 k보다 작을 떄 (더이상 나눌 수 없는 경우)
    if n < k:
        break
    # k로 나누기
    result += 1
    print('n=', n, 'target=', target, 'result=', result)
    n //= k
# 마지막 남은 수에 대해서 1씩 빼기
result += (n-1)
print(result)