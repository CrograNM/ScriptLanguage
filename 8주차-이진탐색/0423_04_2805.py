import sys

# 입력값을 빠르게 받기 위한 설정
input = sys.stdin.readline

# n : 나무의 개수, k : 필요한 나무의 길이
n, k = map(int, input().split())

# 각 나무의 길이를 입력받아 리스트에 저장
lis = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
s = 0
e = max(lis)

# 이진 탐색 수행
while s <= e :
    mid = (s+e)//2    # 이진탐색을 위해 중간값을 구합니다.
    sum = 0
    for i in lis :
        if i > mid :
            sum += i - mid  # mid값보다 큰 나무들의 길이를 sum에 더합니다.
    if sum >=k:         # sum이 가져가려고 하는 길이 k보다 크거나 같으면
        s = mid+1       # mid를 증가시켜서 더 많은 나무를 자릅니다.
    else :
        e = mid-1       # mid를 감소시켜서 덜 자릅니다.
print(e)