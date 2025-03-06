'''

오셀로 재배치 (백준 13413)

<오셀로 의사코드>
N : 5
o1 : 01100
o2 : 01010

for i(N: 0~4):
	o1[i] 와 o2[i] 비교
	같으면 넘어감
	다르면 해당 인덱스 저장 (리스트 생성 후, 모든 인덱스들 저장됨)
		--> index_list = [2, 3] (2, 3번 인덱스가 서로 다름)
만약 인덱스 리스트의 개수 len이
짝수라면 //2를 하고 출력.
홀수라면 //2를 하고 +1 하고 출력.

'''

T = int(input())
for _ in range(T):
    N = int(input()) # 오셀로 말의 개수

    o1 = input()  # string WBBWW
    o2 = input()  # string WBWBW
    # 문자열은 특정 인덱스의 원소 '교체'가 불가능 : 리스트로 변환
    # --> ['W', 'B', 'B', 'W', 'W']처럼 바꾸자

    list_o1 = list()
    list_o2 = list()
    for i in range(N):
        list_o1.append(o1[i])
        list_o2.append(o2[i])

    pass