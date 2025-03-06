'''

백준 10250 문제, ACM 호텔


'''

def reserve(H,W,N): # H, W, N 에 대한 방 번호 반환
    # 1, 1, 1 이면 101
    # 11, 1, 1 이면 1101 -> H에 대해 100을 곱하고 숫자에 따라
    # N에서 H로 나머지 연산을 통해 번호를 구한다
    # H가 6이면 N이 10일 때, 10번재 사람은 4층 (402호)에 입주하게 된다
    count = 1
    for room in range(1, W+1): # room = 1,2,3, ..., W
        for floor in range(1, H+1): # floor = 1,2,3, ..., H
            if count == N:
                return floor * 100 + room
            count += 1
    pass

test_count = int(input())
for _ in range(test_count):
    H, W, N = map(int, input().split())
    print(reserve(H,W,N))