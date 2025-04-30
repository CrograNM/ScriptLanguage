"""
    TUK 0067 - 자산증감
    n일 동안 회사의 순자산이 어떻게 증감했는지를 그림으로 출력하시오

    입력 : 첫줄에 숫자, 둘째줄에 +, -, = 으로 이루어진 문자열
    출력 : '/', '\', '_', '.' 으로 이루어진 행렬 (주식 그래프 그림)
"""

N = int(input())
asset_record = input()
M = [['.']*N]
r = 0   # row
p = '.' # 전날 자산증감 값 관리 변수, previous

for c in range(N):          # col : 0, 1, 2, ... , N-1
    if asset_record[c] == '+':
        if p == '/':        # 전날 자산이 +면 행을 위로 올려야함
            if r == 0:      # 행을 위에 추가(삽입 연산으로 처리)
                M.insert(0,['.']*N)
            else:
                r -= 1
        p = M[r][c] = '/'
    elif asset_record[c] == '-':
        if p == '\\' or p == '_':   # 전날이 감소 혹은 동일하면 행을 내려야함.
            if r == len(M)-1:       # 행 인덱스가 마지막 행을 가리키고 있으면 행을 아래에 추가한다. (맨 뒤쪽에 행 추가)
                M.append(['.']*N)
            r += 1
        p = M[r][c] = '\\'
    else: # '=', equal
        if p == '/': # 전날이 상승일 경우에만 행을 위로 올린다 (/_\ 가 안되니까)
            if r == 0:
                M.insert(0, ['.'] * N)
            else:
                r -= 1
        p = M[r][c] = '_'

# 출력
for r in range(len(M)):
    print(''.join(M[r]))
