
"""
    십자말 풀이 (TUK 0071)

    input : A, B - 2개의 단어 (공백으로 구분됨)
    output : A, B가 각각 공유하는 첫번째 문자를 교차시키며 십자로 출력함
"""

# input
A, B = input().split()

A_index = 0
B_index = 0

# A 검사 (key, A_index, B_index 검출)
for i in range(len(B)):
    B_index = B.find(A[i]) # A단어의 i번째 문자를 B단어에서 찾는다
    if B_index != -1:
        A_index = i
        break

# print(A_index)
# print(B_index)

L = [['.']*len(A) for _ in range(len(B))]
for i in range(len(B)):
    L[i][A_index] = B[i]
for j in range(len(A)):
    L[B_index][j] = A[j]

for i in range(len(B)):
    print(''.join(L[i]))
