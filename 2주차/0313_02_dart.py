
"""
    프로그래머스 다트게임

    1S2D*3T
    1D2S0T
"""

def solution(dartResult):
    number = 0
    score = []
    # dartResult를 순회하며 점수를 기록한다

    for i in dartResult:
        if '0' <= i <= '9': # 점수는 0~10점
            if i == '0' and number == 1:
                number = 10
            else:
                number = int(i) # 0점이냐 10점이냐를 구분하기 위한 과정
            pass
        elif i == 'S':
            number = number ** 1
            score.append(number)
            pass
        elif i == 'D':
            number = number ** 2
            score.append(number)
            pass
        elif i == 'T':
            number = number ** 3
            score.append(number)
            pass
        elif i == '*':
            if len(score) > 1:
                score[-1] = score[-1] * 2
                score[-2] = score[-2] * 2
            else :
                score[0] = score[0] * 2
            pass
        elif i == '#':
            score[-1] = score[-1] * -1
            pass
    return sum(score)

print(solution('1S2D*3T'))  # 37
print(solution('1D2S#10S')) # 9
print(solution('1D2S0T'))   # 3
print(solution('1S*2T*3S')) # 23
print(solution('1D#2S*3S')) # 5
print(solution('1T2D3D#'))  # -4
print(solution('1D2S3T*'))  # 59