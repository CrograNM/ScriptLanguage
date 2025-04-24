"""
    백준 17266 - 어두운 굴다리
    
    시간이 촉박한 문제일 때, 입력 수가 많을 떄, 최소 값을 구하는 문제일 때 등
    이분 탐색을 사용하도록 하자
"""

N = int(input())    # 굴다리의 길이   (1 ≤ N ≤ 100,000)
M = int(input())    # 가로등의 개수   (1 ≤ M ≤ N)

# M 개의 설치할 수 있는 가로등의 위치 x 가 주어진다. (0 ≤ x ≤ N)
x_array = list(map(int, input().split()))

start, end = 1, N    # 가로등의 높이
result = 0

def check(H):
    p = 0
    for x in x_array:
        if p < x - H:
            return False
        p = x + H
    if p >= N:    # 마지막 가로등 오른쪽 범위가 N을 포함해야한다.
        return True
    else:
        return False

# 이진 탐색 수행
while start <= end:     # start와 end는 구하는 값의 범위인듯
    mid = (start + end) // 2
    if check(mid):  # mid 높이로 굴다리 전체를 비추는가?
        result = mid    # 조건을 만족하면 정답 후보
        end = mid - 1   # 가로등 높이를 낮춰서 재검사
    else:
        start = mid + 1 # 가로등 높이를 높여서 재검사 (조건 불만족)
print(result)