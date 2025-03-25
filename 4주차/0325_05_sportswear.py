"""
    프로그래머스 - 체육복

    n: 학생수
    lost: 도난 당한 학생 배열
    reserve: 여벌의 번호 배열
    lost와 reserve의 원소 차이가 +-1이어야 수업을 들을 수 있다.
    체육수업을 들을 수 있는 학생의 최댓값을 리턴
"""

# 초기값 answer = n - len(lost)이다.
# lost 리스트의 +-1값이 reserve 리스트에 있으면 꺼내고, answer += 1을 한다.
# lost 리스트가 비거나, reserve 리스트가 비게 되면 결과를 리턴한다.

def solution(n, lost, reserve):
    answer = n - len(lost)
    i = 0
    while True:
        if len(reserve) == 0 or len(lost) == 0:
            break
        if lost[i] - 1 in reserve:
            reserve.remove(lost[i] - 1)
            lost.remove(lost[i])
            answer += 1
        elif lost[i] + 1 in reserve:
            reserve.remove(lost[i] + 1)
            lost.remove(lost[i])
            answer += 1
        else : # 둘 다 없는 경우 다음 인덱스로 이동
            i += 1
            if i >= len(lost):
                break
    return answer