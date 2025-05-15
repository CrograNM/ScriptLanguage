"""
    눈송이
"""

"""
    snow[i][j] 가 가운데일때,
    
    snow[i-1][j]
    snow[i+1][j]
    snow[i][j-1]
    snow[i][j+1]
    snow[i-1][j+1]
    snow[i+1][j-1]
    snow[i-1][j-1]
    snow[i+1][j+1]
    각 방향에서 맞는 문자가 있어야함. 없거나 인덱스 범위를 벗어나면 바로 탈출 후 최댓값 반환
"""

"""
    1. 입력
    
    2. 모든 눈송이의 가운데 위치를 찾고 저장한다
    
    3. 각 가운데 위치에서 위의 포문을 돌린다
"""

P = int(input())
for _ in range(P):
    n, m = map(int, input().split())
    snow = []
    for _ in range(n):
        snow.append(list(input()))
    #find midle
    middle_i = []
    middle_j = []
    for i in range(n):
        for j in range(m):
            if snow[i][j] == '+':
                middle_i.append(i)
                middle_j.append(j)

    # 각 가운데 위치에서 검사
    m_size = [0]
    k=1
    for i, j in middle_i, middle_j:
        while(True):
            if i-k<0:
                break
            if j-k<0:
                break
            if i+k > n-1:
                break
            if j+k > m-1:
                break
            if snow[i - k][j] != '-':
                break
            if snow[i + k][j] != '-':
                break
            if snow[i][j - k] != '|':
                break
            if snow[i][j + k] != '|':
                break
            if snow[i - k][j + k] != '\\' :
                break
            if snow[i + k][j - k] != '/':
                break
            if snow[i - k][j - k]!= '/':
                break
            if snow[i + k][j + k] != '\\' :
                break
            k+=1
            m_size[k-1] += 1