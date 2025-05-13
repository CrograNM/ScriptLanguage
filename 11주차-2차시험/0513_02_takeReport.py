"""
    프로그래머스 - 신고 결과 받기
"""
"""
    "유저 ID" 리스트
    "유저가 신고한 유저" 리스트
    k 번 신고 당하면 정지
    
    정지 사실 메일 : 유저가 신고한 유저가 정지 되었음을 알림 (정지된 유저를 신고한 모든 유저에게 발송)
    정지 메일 : 정지된 유저에게 발송하는 메일
    
    위 메일 횟수 두개를 합쳐서 총 횟수를 리턴
    
    여러번 신고해도 처리 결과는 1이어야 함. 
        -> 어떤 유저가 특정 유저를 신고한 사실을 저장
    
    list1 ["유저1"] = set(유저2 신고함, 유저3 신고함, 유저4 신고함)
    list2 ["유저1"] = 몇 번 신고 당함 -> list1에서 만들어야 함
    list3 ["유저1"] = 받는 메일 횟수 (result) id_list를 통해서 
    list2에서 순회 -> list1 전체 순회를 통해 set에 해당 유저가 있으면 list3에 횟수 추가 
                        and "신고당한 유저"의 횟수도 list3에서 추가
"""
def solution(id_list, report, k):
    from collections import defaultdict

    report_list = defaultdict(set)        # 누가 누구를 신고했는지
    reported_count = defaultdict(int)     # 각 유저가 몇 번 신고당했는지
    mailed_count = defaultdict(int)       # 각 유저가 받은 메일 수

    # 1. 신고 정보 저장
    for r in set(report):  # 중복 제거
        reporter, reported = r.split()
        report_list[reporter].add(reported)

    # 2. 신고당한 횟수 계산
    for reporter in report_list:
        for reported in report_list[reporter]:
            reported_count[reported] += 1

    # 3. 메일 발송 (정지된 유저를 신고한 유저에게 메일)
    for reporter in report_list:
        for reported in report_list[reporter]:
            if reported_count[reported] >= k:
                mailed_count[reporter] += 1

    # 4. id_list 순서대로 결과 반환
    return [mailed_count[user] for user in id_list]

# res : [2, 1, 1, 0]
print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],
               2))

# res : [0, 0]
print(solution(["con", "ryan"],
               ["ryan con", "ryan con", "ryan con", "ryan con"],
               3))
