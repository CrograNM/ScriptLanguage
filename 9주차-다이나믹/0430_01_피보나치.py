
# DP 테이블
d = [0]*100
def fibo(x):
    if x == 1 or x == 2:
        return 1

    # 이미 계산한 결과가 있다면 재사용
    if d[x] != 0:
        return d[x]

    # 아직 계산하지 않은 문제라면 점화식으로 재귀호출
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))