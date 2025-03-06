f = 157.93
print(type(f))

f = 0.3 + 0.6
print(f) # not 0.9

print(round(f, 3)) # 반올림, round(변수, 소수점 자리)

# 연산들
print(4/3) # 실수 나눗셈
print(4//3) # (나머지 버리기) 나눗셈
print(13 % 10) # 나머지 연산
print(2**0.5) # 거듭제곱

# 리스트 자료형
l = [1,2,4.5, 'korea', [1,3]]
print(type(l))
print(l) # 리스트 전체 출력
print(l[0]) # 인덱스 0부터 시작
print(l[-1]) # 음수 인덱스가 가능함

# 리스트 슬라이싱
print(l[1:4]) # 1번 인덱스부터 4번 인덱스 전까지
print(l[0:4])   # 0번 인덱스는
print(l[:4])    # 생략 가능
print(l[:-1]) # 마지막 원소 전까지

print(l)
l.reverse()
print(l)
print(l[::-1])
print(l[-1:0:-1]) # 시작(포함) : 끝(미포함) : 간격