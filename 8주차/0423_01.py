"""
    이진 탐색
"""

# 이분탐색 재귀함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return mid

# n 원소 개수, target 찾고자 하는 값
n, target =map(int,input().split())
# 정렬된 전체 원소 입력받기
array = list(map(int, input().split()))
result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않는다')
else:
    print('원소 : ', result + 1, '번째 위치')

