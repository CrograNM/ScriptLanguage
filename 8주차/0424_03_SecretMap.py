"""
    프로그래머스 - 비밀지도
"""


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = arr1[i] | arr2[i]   # 비트 or 연산
        s = ''                              
        for j in range(n):      # a에서 n 비트를 꺼낸다
            if a & 1:           # 제일 오른쪽 비트가 1이면
                s = '#' + s
            else:
                s = ' ' + s
            a = a >> 1          # a를 오른쪽 1비트 쉬프트
        answer.append(s)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))