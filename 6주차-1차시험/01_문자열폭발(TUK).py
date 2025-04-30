
"""
    문자열 1
    문자열 2

    문자열 1에서 문자열 2 삭제 : 문자열 3으로 재생성
    문자열 3에서 다시 문자열 2 삭제 (못찾을 때 까지)
"""

str = input()
bomb = input()
bomb_len = len(bomb)

while True:
    idx = str.find(bomb)
    if idx == -1:
        break

    # 슬라이싱으로 문자열 재생성
    str = str[:idx] + str[idx + bomb_len:]

print(str)
