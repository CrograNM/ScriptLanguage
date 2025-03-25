"""
    모험가 길드
"""

n = int(input())                        # 5
data = list(map(int, input().split()))  # 2 3 1 2 2
data.sort() # 공포도 오름차순 정렬
result = 0  # 그룹의 총 수
count = 0   # 현재 그룹의 모험가 수
for i in data: # 공포도 낮은 것부터 하나씩 꺼내서
    count += 1 # 현재 그룹에 모험가 1명 추가
    if count >= i:  # 현재 그룹 모험가 수가 현재 공포도 이상이면, 증가
        result += 1 # 그룹화 시키고
        count = 0   # 현재 그룹의 모험가 수는 초기화
print(result)       # 총 그룹 수 출력