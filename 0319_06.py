"""
    시각, 완전탐색
    N(0 ~ 23)입력, 00시 00분 00초 부터 N시 59분 59초 까지 중에서 3이 들어간 시각의 수
"""
N = int(input())
count = 0
for h in range(N+1):        # h=0,1,2,...,N
    for m in range(60):     # m=0,1,2,...,59
        for s in range(60): # s=0,1,2,...,59
            if '3' in str(h) + str(m) + str(s):
                count += 1
print(count)