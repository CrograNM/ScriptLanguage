"""
    문자열 재정렬
    K1KA5CB7 -> ABCKK13
"""

data = input()  # 알파벳 대문자와 숫자로 이루어진 문자열
result = []     # 알파벳 문자들을 갖는 리스트
value = 0       # 숫자의 합

# 문자를 하나씩 확인
for x in data:
    if x.isalpha():         # 알파벳이면
        result.append(x)    # result = ['K', 'A', ...]
    else :                  # 숫자이면                
        value += int(x)     
        
result.sort()
if value != 0:
    result.append(str(value))
print(''.join(result))


