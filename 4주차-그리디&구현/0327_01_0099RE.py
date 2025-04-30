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
from itertools import combinations

N = int(input())
foods = [list(map(int, input().split())) for _ in range(N)]
#print(foods)
std = list(map(int, input().split()))
#print(std)

res = 0
for i in range(1,4): # i는 1,2,3 
    
    if i > N: # N이 3보다 작은 경우도 생각해야함
        break 
        
    for food_comb in combinations(foods, i): # food들이 튜플로 묶여서 food_comb에 저장된다.
        # print(food_comb)
        sof = [0, 0, 0]
        for food in food_comb:  # 튜플에서 food를 꺼내며 각 원소들의 합을 저장한다.
            sof[0] += food[0]
            sof[1] += food[1]
            sof[2] += food[2]
        cal = sof[0]*4 + sof[1]*4 + sof[2]*9
        if sof[0] <= std[0] and sof[1] >= std[1] and sof[2] <= std[2] and cal <= std[3]:
            res += 1
print(res)