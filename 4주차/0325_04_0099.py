"""
    TUK 0099 - 균형 잡힌 영양소

    입력 :
    첫째 줄에 음식의 개수 N
    다음 N개 줄에 걸쳐서 각 음식의 탄수화물, 단백질, 지방의 양
    마지막 줄에는 기준치가 되는 탄수화물, 단백질, 지방, 열량의 양

    출력 :
    음식을 기준치(마지막 줄)에 맞게 조합하여 만들 수 있는 식단의 가짓수(정수) 출력

    기준치에 적합한 경우 :
        음식을 3개 '까지' 포함할 수 있다.
        탄수화물의 합 : 기준치가 되는 탄수화물 '이하'
        단백질의 합  : 기준치가 되는 단백질 '이상'
        지방의 합   : 기준치가 되는 지방 '이하'
        총 열량    : 기준치가 되는 열량 '이하'
"""

N = int(input())
foods = [ list(map(int, input().split())) for _ in range(N) ]   # 음식들 2차원 배열 생성
# foods[i][j] - [i]:Food 종류, [j]:영양소 종류(탄,단,지)
std = list(map(int, input().split()))                           # 기준: 탄, 단, 지, 칼로리 리스트

# 기준치 검사 함수
def isGoodFoods(sum_of_food, standard):
    if sum_of_food[0] > standard[0]:
        return False
    if sum_of_food[1] < standard[1]:
        return False
    if sum_of_food[2] > standard[2]:
        return False
    if (sum_of_food[0] * 4 + sum_of_food[1] * 4 + sum_of_food[2] * 9 
            > standard[3]): # (열량 = 탄수화물 * 4 + 단백질 * 4 + 지방 * 9)
        return False
    #print(sum_of_food, sum_of_food[0] * 4 + sum_of_food[1] * 4 + sum_of_food[2] * 9)
    return True

# 경우의 수 검사하기
res = 0
# 음식 한개 식단
for i in range(N):
    if isGoodFoods(foods[i], std):
        res += 1

# 음식 두개 식단
for i in range(N):
    for j in range(i+1, N):
        if i != j:
            sof = [foods[i][_] + foods[j][_] for _ in range(len(foods[i]))]
            if isGoodFoods(sof, std):
                res += 1

# 음식 세개 식단
for i in range(0, N):
    for j in range(i+1, N):
        if i != j:
            for k in range(j+1, N):
                if i != k and j != k:
                    sof = [foods[i][_] + foods[j][_] + foods[k][_] for _ in range(len(foods[i]))]
                    if isGoodFoods(sof, std):
                        res += 1

# 출력
print(res)
