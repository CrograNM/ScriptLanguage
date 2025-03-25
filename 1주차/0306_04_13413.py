'''

오셀로 재배치 (백준 13413)

0 1 1 0 0
1 0 1 0 0
-> 0,1 개수가 동일하지만, 순서가 다름.
-> 서로 다른 0번, 1번 인덱스를 리스트에 저장

'''

T = int(input())
for _ in range(T):
    N = int(input()) # 오셀로 말의 개수
    before = input() # 초기 상태
    after = input()  # 목표 상태

    ''' 다른 부분을 검사하며 해당 부분을 저장 후, 저장된 B/W 횟수 중 더 많은 횟수가 정답 '''

    count_B = 0
    count_W = 0

    for i in range(N):
        if before[i] != after[i]:
            if before[i] == 'W': count_W+= 1
            else : count_B += 1

    print(max(count_B, count_W))
