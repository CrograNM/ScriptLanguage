"""
    왕실의 나이트
    a1 입력 -> 2 출력
    c2 입력 -> 6 출력
"""

# 현재 나이트 위치 입력 a1, c5 등
data = input()
r = int(data[1])
c = ord(data[0]) - ord('a') + 1     # a:h -> 1:8
# 8가지 방향 벡터
steps = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,-2), (1,-2), (-1,2), (1,2)]
# 8가지 각 위치로 이동 가능한지 확인
result = 0
for step in steps:
    nr = r + step[0]
    nc = c + step[1]
    if 1 <= nr <= 8 and 1 <= nc <= 8:
        result += 1
print(result)
