"""
    TUK 0063 : 행렬 게임
"""
"""
    a, b을 입력받아 (a*b) 행렬을 만든다.
    
    출력 :
        M,  
            a*b 행렬
        R, 
            오른쪽으로 회전한 M행렬
        L, 
            왼쪽으로 회전한 M행렬
        T, 
            M의 전치행렬 
"""

def print2DList(list):
    for i in range( len(list) ):
        for j in range( len(list[0]) ):
            if j == len(list[0]) - 1:
                print(list[i][j])
            else:
                print(list[i][j], end=' ')

A,B = map(int, input().split())

"""
M
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
"""
print('M')
M = [[ r*B + c + 1 for c in range(B)] for r in range(A) ]
print2DList(M)

"""
R
11 6 1          00 01 02
12 7 2          10 11 12
13 8 3          20 21 22
14 9 4          30 31 32
15 10 5         40 41 42
"""
print('R')
R = [[ M[r][c] for r in range(A-1, -1, -1) ] for c in range(B)]   # 위에서 B에 해당하는 원소를 c로 썼으니 똑같이 한다
print2DList(R)
# num = 1
# R = [[0]*A for _ in range(B)]
# for i in range(1, A+1):      # 3
#     for j in range(B):  # 5
#         R[j][-i] = num
#         num+=1
# print2DList(list)

"""
L
5 10 15         00 01 02
4 9 14          10 11 12
3 8 13          20 21 22
2 7 12          30 31 32
1 6 11          40 41 42
"""
print('L')
num = 1
L = [[0]*A for _ in range(B)]
#print(list)
for i in range(A):           # 3
    for j in range(1, B+1):  # 5
        L[-j][i] = num
        num+=1
print2DList(L)

"""
T
1 6 11          00 01 02
2 7 12          10 11 12
3 8 13          20 21 22
4 9 14          30 31 32
5 10 15         40 41 42
"""