"""
    백준 11047 - 동전 0 문제

    input : 첫째 줄에 N, K 정수, 둘째 줄에 동전들
    output : k원을 만드는데 필요한 동전 개수의 최솟값 출력
"""

N,K = map(int, input().split())
coins = [int(input()) for _ in range(N)] # N개의 동전 리스트를 입력받는다.
coins.reverse() # 내림차순
result = 0
for coin in coins :
    result += K // coin
    K %= coin
    if K == 0:
        break
print(result)