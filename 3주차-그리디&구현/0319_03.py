"""
    곱하기 혹은 더하기
"""

data = input() # 숫자 문자열 입력 02984
# 첫번째 문자를 숫자로 변경
result = int(data[0])
for i in range(1, len(data)): #i = 1,2,3,...,len-1
    # 두 수 중에서 하나라도 0,1 인 경우라면
    num = int(data[i])
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
print(result)