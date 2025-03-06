
# 실수 자료형
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

# 리스트 컴프리헨션
ll = [i for i in range(10)]
print(ll)
lll = [i for i in range(20) if i%2 == 1] # 조건식 넣을 수도 있다 (홀수만 추가)
print(lll)
llll = [i**2 for i in range(1,11)]
print(llll)

l2d = [[(row, col) for col in range(3)] for row in range(2)] # 2차원 배열도 가능
print(l2d[:1])
print(l2d[1:])
array = [[0]*3 for _ in range(3)]
# array2 = [[0]*3] * 3 # wrong way
print(array)

# 문자열
data = "Don't you know \"python\""
print(data)
data = 'hello '
data2 = 'world'
#data[1] = 'x' # 문자열은 특정 인덱스의 원소 '교체'가 불가능
print(data + data2) # 문자열에 연산이 가능
print(len(data2)) # len 함수 : 리스트 형식 자료형들의 사이즈를 알려줌

# 튜플
t = 2,3 # 한번 선언된 값 변경 불가, 리스트에 비해 상대적으로 공간효율적
print(type(t))
print(t)
print(t[0:2])

# 사전 자료형
d = {'사과':'apple', '바나나':'banana', '키위':'kiwi'}
print(d['사과'])
#print(d[0]) 불가?
print(d)
print(d.keys())
print(d.values())