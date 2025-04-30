
"""
    W B W B W B W B
    B W B W B W B W
    W B W B W B W B
    B W B W B W B W
    W B W B W B W B
    B W B W B W B W
    W B W B W B W B
    B W B W B W B W

    입력 :
        .F.F...F
        F...F.F.
        ...(생략)
    
    --> for문으로 한줄씩 번갈아가면서 검흰검흰과 흰검흰검을 체크하면서 숫자세기 (홀짝으로 하면 될듯)
"""

count = 0
WB_start = ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'] # 체스판 각 행의 시작지점 타입
for type in WB_start:
    if type == 'W':
        flag = 0
    else :
        flag = 1
    list = input()  # .F.F...F
    for i in range(8):
        # type = 'W' and 짝수 인덱스면 하얀칸
        # type = 'B' and 홀수 인덱스면 하얀칸
        if i % 2 == flag and list[i] == 'F':
            count += 1

print(count)

