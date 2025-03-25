"""
    백준 2798 - 블랙잭 문제 (조합 문제)
    N 장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.

    5 21
    5 6 7 8 9
    -> 21
"""

N,M = map(int, input().split())
cards = list(map(int, input().split()))
#print(cards)
# 위 리스트에서 M에 최대한 가까운 3개 숫자의 합을 출력하라

# 모든 3개 숫자 합의 경우를 구하고 가까운close 값을 구한다?
# N개의 숫자 중 3개씩 묶는 경우의 수는 N * N-1 * N-2
sums = []
for i in range(N):
    n1 = cards[i]
    for j in range(N):
        if i != j:
            n2 = cards[j]
            for k in range(N):
                if j != k and i != k:
                    n3 = cards[k]
                    sums.append(n1 + n2 + n3)
# print(sums)
# print(len(sums))

# 가장 가까운 수 구하기
close = 0
for i in range(len(sums)):
    if M < sums[i]:
        continue
    elif M == sums[i]:
        close = M
        break
    # close, M의 차의 절댓값이
    # sums[i], M의 차의 절댓값 보다 크면 close가 바뀐다.
    elif abs(M - close) > abs(M - sums[i]):
        close = sums[i]

# 출력
print(close)