"""
    TUK - b진법
"""

"""
    b 진수 숫자(b>0)의 모든 숫자는 0과 b-1 사이의 숫자
    예를 들어 기수 4를 가지는 4진수 숫자는 3312 또는 30을 쓸 수 있다.
    
    b진수숫자가 dn-1 ... d0이고 각 di가 0과 b-1 사이에 있다고 가정하면 
    그 숫자의 10진수는 다음과 같이 계산할 수 있다.
    dn-1 ... d0 (b진수) 
        = d0 + (d1 * b) + (d2 * b^2) + ... + 
            (di * b^i) + ... + (dn-1 * b^(n-1)) (10진수)
           
    입력: 
    첫 번째 행에는 3 개의 정수 b, N 및 M이 포함되며 여기서 b는 기수
        N과 M은 주어진 두 숫자의 b진수 표현의 숫자 개수
    두 번째 줄은 N 개의 공백으로 구분 된 정수로써 
        DN-1 DN-2 ... D0은 첫 번째 숫자의 b진수 표현을 제공
    세 번째 줄은 M 개의 공백으로 구분 된 정수로써 
        EM-1 EM-2 ... E0는 두 번째 숫자의 b진수 표현을 제공
    
    당신의 임무는 기수 b와 b진수 숫자 A와 B가 제공되면 A × B의 b 진수 숫자를 출력하는 것
    출력:
    첫 번째 행은 곱의 b 진수 숫자 개수를 나타내는 단일 정수 L
    두 번째 줄에는 b 진수 표현을 제공하는 L 공백으로, 1구분 된 정수가 포함
"""

def BtoD(L, b): # b진수 정수 리스트 L을 10진수로 변환 후 반환
    # L = [3, 3, 1, 2], b = 4
    result = 0
    # result = (((((0*4) + 3)*4 + 3)*4 + 1)*4 + 2)
    for n in L:
        result = result*b + n
    return result

def DtoB(N, b): # 10진수 N을 b진수 리스트로 변환 후 반환
    L = [] # b진수 리스트 초기화
    while N:
        L.insert(0, N % b)
        N = N // b
    return L

b, N, M = map(int, input().split())
A = list(map(int, input().split())) # A = [3, 3, 1, 2]
B = list(map(int, input().split())) # B = [3, 0]

A10 = BtoD(A, b) # A를 10진수로 전환
B10 = BtoD(B, b) # B를 10진수로 전환
L = DtoB(A10 * B10, b)
print(len(L))
for n in L:
    print (n, end=' ')
print()