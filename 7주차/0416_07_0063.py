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

print('M')
M = [[ r*B + c + 1 for c in range(B)] for r in range(A) ]
print2DList(M)

print('R')
R = [[ M[r][c] for r in range(A-1, -1, -1) ] for c in range(B)]   # 위에서 B에 해당하는 원소를 c로 썼으니 똑같이 한다
print2DList(R)

print('L')
L = [[ M[r][c] for r in range(A) ] for c in range(B-1, -1, -1)]
print2DList(L)

print('T')
T = [[ M[r][c] for r in range(A) ] for c in range(B)]
print2DList(T)