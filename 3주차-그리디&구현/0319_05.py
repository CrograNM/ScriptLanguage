"""
    구현 - 상하좌우
"""

# 5
# R R R U D D
# 결과 : 3 4

n = int(input())            # N 입력
r, c = 1, 1 # row=행, col=열
plans = input().split()     # ['R', 'R', 'R', 'U', 'D', 'D']
# LRUD 방향벡터
dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']
# 이동 계획 하나씩 확인
for plan in plans: # plan = 'R', 'R', 'U', 'D' ...
    # 이동 후의 좌표 구하기
    i = move_types.index(plan)
    nr = r + dr[i]
    nc = c + dc[i]
    if 1 <= nr <= n and 1 <= nc <= n:
        r,c = nr,nc
print(r,c)
