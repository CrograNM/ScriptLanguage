import sys
input = sys.stdin.readline


# n 떡의 개수, m 손님이 요청한 떡 길이
n, m = map(int, input().split())

# 떡 배열
array = sorted(list(map(int, input().split())), reverse=True)
#print(array)
start = 0
end = 1000000000 

# 조건을 만족하는 절단기 최대 높이
result = 0

# 이분 탐색
while start <= end:
    mid = (start + end) // 2
    total = 0 # 자르고 남은 떡길이 변수
    for x in array:
        if x > mid: # 떡길이가 mid(절단기)보다 크면 잘라서 total에 더한다
            total += (x - mid)
        else :
            break
    if total < m:   # 조건을 만족하지 않는다 (절단기를 작게 해야함)
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)