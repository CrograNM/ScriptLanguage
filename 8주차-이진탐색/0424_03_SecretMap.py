"""
    프로그래머스 - 비밀지도
"""


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        save = bin(arr1[i] | arr2[i])
        l = list(save[2:])
        #print(l)
        map = ''
        for s in l:
            if s == '0':
                map = map + ' '
            elif s == '1':
                map = map + '#'
        answer.append(map)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))