'''

백준 1764번 듣보잡 문제

듣지 못한 사람의 명단이 주어짐
보지 못한 사람의 명단이 주어짐

듣지도 보지도 못한 사람의 명단을 구하는 프로그램 작성
(집합 자료형 사용)
출력은 사전 순으로 출력 (집합을 리스트로 바꿔서, sort로 출력)

'''

N,M = map(int, input().split())

D = set()
for _ in range(N): # 듣지 못한 사람 집합
    D.add(input())

B = set()
for _ in range(M): # 보지 못한 사람 집합
    B.add(input())

# 교집합 (intersection) : 듣지도 보지도 못한 사람 집합
C = list(D.intersection(B))
C.sort()
print(len(C))
for person in C:
    print(person)