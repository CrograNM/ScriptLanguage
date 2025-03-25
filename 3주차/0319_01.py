"""
    coin change
"""

n = 1260
count = 0
# 큰 단위 동전부터 차례로 확인
array = [500, 100, 50, 10] # 큰 단위의 화폐가 작은 단위의 배수이기 때문에 그리디가 가능하다.
for coin in array:
    count += n // coin # 해당 동전으로 거슬러 줄 수 있는 동전 개수
    print(coin, '동전', n//coin, '개')
    n %= coin
print(count)