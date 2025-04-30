"""
    두 배열의 원소교체
"""

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()                # a는 오름차순 정렬 1, 2, 3 ... 작은거 순서
b.sort(reverse=True)    # b는 내림차순 정렬 5, 4, 3 ... 큰거 순서

# 첫번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(sum(a))