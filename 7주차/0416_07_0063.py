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
"""
M
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
R
11 6 1
12 7 2
13 8 3
14 9 4
15 10 5
L
5 10 15         00 01 02
4 9 14          10 11 12
3 8 13          20 21 22
2 7 12          30 31 32
1 6 11          40 41 42
T
1 6 11
2 7 12
3 8 13
4 9 14
5 10 15
"""

A,B = map(int, input().split())

print('M')
num = 1
for i in range(A):
    for j in range(B):
        print(num, end=' ')
        num += 1
    print()
print('R')

list = [[0]*A for _ in range(B)]
print(list)