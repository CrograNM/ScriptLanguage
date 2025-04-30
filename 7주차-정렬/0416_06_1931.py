"""
    백준 1931 : 회의실 배정
"""

"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

    튜플로 이뤄지는 리스트를 만들어서 정렬로 푼다?
"""
# L = [(1,2),(1,3),(2,2),(0,1)]
# L.sort(key=lambda x:(x[1],x[0])) # 정렬의 기준을 여러개 순서를 정해서 정렬 가능
# # L.sort(key=lambda x:(-x[1],-x[0])) # 내림차순
# print(L)

N = int(input())
L = []
for _ in range(N):
    source = tuple(map(int, input().split()))
    L.append(source)
L.sort(key=lambda x:(x[1],x[0]))    
# 회의를 끝나는 시간 순서로 정렬하고, 끝나는 시간이 같은 경우 시작 순서로 정렬한다
#print(L)

count = []
end = 0
for l in L:
    if end <= l[0]:         # 이전 회의 종료 시간보다 회의 시작시간이 크거나 같으면
        end = l[1]          # 회의 종료 시간이 변경되고
        count.append(l)     # 배정 리스트에 추가한다.
#print(count)
print(len(count))