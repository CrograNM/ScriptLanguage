
"""
    십자말 풀이 (TUK 0071)

    input : A, B - 2개의 단어 (공백으로 구분됨)
    output : A, B가 각각 공유하는 첫번째 문자를 교차시키며 십자로 출력함
"""

"""
A의 문자열 리스트가 있다면,
B를 검사하여 A 문자열에 포함되는 문자가 있는지 하나하나씩 검사.
가장 첫번째로 중복되는 문자와 그 인덱스를 저장 (key, B_index)
이제 A_index = A.find(key)를 통해 인덱스 검출

출력단계:
len(A), len(B)를 사용하고,
이중 for문을 통해 출력 시작
"""

# input
A, B = input().split()

A_index = 0
B_index = 0
key = ''

# B 검사 (key, A_index, B_index 검출)
for i in range(len(B)):
    is_break = False
    for j in range(len(A)):
        if B[i] == A[j]:
            A_index = j
            B_index = i
            key = B[i]
            is_break = True
            break
    if is_break:
        break

# print(key)
# print(A_index)
# print(B_index)

# 출력 단계
for i in range(len(B)):
    if i == B_index:
        print(A)
    else :
        text = ''
        for j in range(len(A)):
            if j != A_index:
                text = text + '.'
            else:
                text = text + B[i]
        print(text)
