"""
    05_투포인터 - 특정한 합을 가지는 부분연속수열 찾기
"""

n = 5                   # 데이터 개수
m = 5                   # 찾고자 하는 부분합
data = [1,2,3,2,5]      # 전체 수열
count = 0
interval_sum = 0
end = 0

# start 를 차례로 증가 시키며 반복
for start in range(n): # start = 0,1,2,...,n-1
    # end 를 가능한 만큼 이동 시킨다.
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1

    # 부분 합이 m이면 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)