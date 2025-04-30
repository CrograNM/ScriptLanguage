"""
    프로그래머스 - 실패율
"""
"""
    실패율 = 스테이지 도달했지만 클리어 못한 플레이어 수 / 스테이지 도달한 플레이어 수
    전체 스테이지 수 N
    사용자가 멈춰있는 스테이지 번호가 담긴 배열 stages
    실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 
    
    [2, 1, 2, 6, 2, 4, 3, 3] -> [3,4,2,1,5]
    (1) 1/8 : (1의 개수) 1, (1 이상의 개수) 8    
    (2) 3/7 : (2의 개수) 3, (2 이상의 개수) 7   
    (3) 2/4 : (3의 개수) 2, (3 이상의 개수) 4  
    (4) 1/2 : (4의 개수) 1, (4 이상의 개수) 2
    (5) 0   : (5의 개수) 0, (5 이상의 개수) 1
    튜플 (스테이지, 실패율)로 내림차순, 실패율 우선 내림차순
    튜플에서 스테이지만 순서대로 꺼내서 배열을 리턴
"""
from collections import Counter

def solution(N, stages):
    counter = Counter(stages)

    # 튜플 (스테이지, 실패율) 리스트 만들기
    list = []
    info = [0] * (N + 2)
    for stage in stages:
        info[stage] += 1

    for i in range(1, N+1):
        # i 보다 높은 스테이지 개수 세기
        i_upper_count = sum(info[i:])
                
        # 실패율 = i의 개수 / i 이상의 수
        fail_rate = 0
        if i_upper_count != 0:
            fail_rate = counter[i] / i_upper_count
        list.append( (i, fail_rate) )

    # 실패율 우선 내림차순
    list.sort(key= lambda x: x[1], reverse=True)
    
    # 정답 리턴
    answer = [ l[0] for l in list ]
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))