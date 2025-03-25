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
    # 여벌이 있지만 도난당한 학생을 제외
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    answer = n - len(lost_set)

    for l in sorted(lost_set):  # 정렬된 상태에서 작은 번호부터 확인
        if l - 1 in reserve_set:
            reserve_set.remove(l - 1)
            answer += 1
        elif l + 1 in reserve_set:
            reserve_set.remove(l + 1)
            answer += 1

    return answer
