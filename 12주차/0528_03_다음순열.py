"""
    TUK 다음순열
"""

def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return sorted(arr)
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i+1:] = reversed(arr[i+1:])
    return arr

N, K = map(int, input().split())
for _ in range(K):
    perm = list(map(int, input().split()))
    result = next_permutation(perm)
    print(*result, end=' \n')  # 공백 끝 포함