'''

오셀로 재배치 (백준 13413)

'''

def job1(N, o1, o2):
    pass

def job2(N, o1, o2):
    pass

def print_min(a,b):
    print(min(a,b))

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