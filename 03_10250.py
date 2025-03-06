'''

백준 10250 문제, ACM 호텔

'''

def reserve(H,W,N): # H, W, N 에 대한 방 번호 반환
    ''' 이중 for문이 아니라 나머지, 몫 연산을 통해 방 번호를 구할 수 있지 않나? '''
    # H가 6이고 N이 6일 때, 601호에 입주하게된다.
    # (N이 H의 배수인 경우 보정 필요)

    floor = N % H
    if floor == 0:
        floor = H  # 0층이 아닌 최상층으로 변경
    room_num = (N - 1) // H + 1  # N이 H의 배수일 때 보정
    return floor * 100 + room_num


test_count = int(input())
for _ in range(test_count):
    H, W, N = map(int, input().split())
    print(reserve(H,W,N))