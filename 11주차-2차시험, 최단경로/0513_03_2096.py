import sys
input = sys.stdin.readline

N = int(input())
prev_max = [0] * 3
prev_min = [0] * 3

a, b, c = map(int, input().split())
prev_max = [a, b, c]
prev_min = [a, b, c]

for _ in range(N - 1):
    a, b, c = map(int, input().split())

    # 이전 상태만을 참조해서 새로운 상태 계산
    curr_max = [
        a + max(prev_max[0], prev_max[1]),
        b + max(prev_max[0], prev_max[1], prev_max[2]),
        c + max(prev_max[1], prev_max[2])
    ]
    curr_min = [
        a + min(prev_min[0], prev_min[1]),
        b + min(prev_min[0], prev_min[1], prev_min[2]),
        c + min(prev_min[1], prev_min[2])
    ]

    # 현재 결과를 이전으로 덮어씀
    prev_max = curr_max
    prev_min = curr_min

print(max(prev_max), min(prev_min))
