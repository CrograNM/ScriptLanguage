"""
    백준 3273 - 두 수의 합
"""
"""
    n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. 
    ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 자연수이다. 
    
    자연수 x가 주어졌을 때, 
    ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 
    (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.
"""

n = int(input())
data = map(int, input().split())
x = int(input()) # 찾고자 하는 합

data = sorted(data)
print(data)

count = 0
interval_sum = 0
end = 0

# start 를 차례로 증가 시키며 반복
for start in range(0, n): # start = 0,1,2,...,n-1
    # end 를 가능한 만큼 이동 시킨다.
    print(start)
    while interval_sum < x and end < n:
        interval_sum = data[start] + data[end]
        print(start, interval_sum)
        if interval_sum > x:
            end -= 1
        else:
            end += 1
    # 부분 합이 m이면 카운트 증가
    if start < end and interval_sum == x:
        count += 1
    interval_sum = 0

print(count)