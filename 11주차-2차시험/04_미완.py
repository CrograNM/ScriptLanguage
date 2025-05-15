"""
계딴 오르기
개미 전사랑 비슷
"""
"""
6 계단 개수
10
20
15
25
10
20
"""

N = int(input()) # 6
array = []
array.append(0)
for _ in range(N):
    array.append(int(input()))

"""
    dp[i] = 각 계단에 도달 했을 때의 최대 점수 (연속 세칸 오르기는 제한 된다)
    dp[i] = array[i] + 이전 계단까지의 합이냐, 한칸 더 이전 계단까지의 합이 더 크냐
    근데 이전에 2칸을 연속으로 올랐으면 취소하고 차선책으로 이동
    dp[i] = array[i] + max(dp[i-1], dp[i-2])
"""

dp = [0]*(300+1)
count = [0]*(300+1)

dp[0] = 0
dp[1] = array[1]
dp[2] = array[2]
count[0] = 0
count[1] = 1
count[2] = 1

for i in range(1, N+1):
    if count[i-1] == 2:
        dp[i] = dp[i - 2] + array[i]
        count[i] = 1

    elif count[i-1] < 2:
        if dp[i-1] < dp[i - 2]:
            dp[i] = dp[i - 2] + array[i]
            count[i] = 1
        else:
            dp[i] = dp[i - 1] + array[i]
            count[i] = count[i - 1] + 1
    # i-1이라는 선택지를 뺄 수 있어야 함

print(dp[N])
