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

----- 위에는 실패 -----
지금 최소 횟수 자체만 구하면 되는 방식으로 구하는 중
7
0000000
0101010
의 경우,
0이 7개인데, 목표 상태는 0:4개, 1:3개이다.
1의 개수가 부족하므로 목표 상태가 되기 위해서는 무조건 바꾸는 행위가 있어야 한다.

4
1100
0010
의 경우, 목표와 0,1의 개수도 다르고 위치도 바꿔야 한다.

첫번째로, 목표의 0, 1 개수를 위한 색 변경 작업 : 1회에 +1
만약 목표와 0, 1 개수가 동일하다면
두번째로, 위치만 다른 경우 위치 변경 작업: 인덱스 개수 //2

110100
001011 -> 0 1 개수가 같고 자리만 6자리가 다름 -> 최소 3회

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

    index_list = list()
    for i in range(N):
        if (list_o1[i] != list_o2[i]):
            index_list.append(i)

    if (len(index_list) % 2 == 0):
        print(len(index_list) // 2)
    else:
        print(len(index_list) // 2 + 1)
