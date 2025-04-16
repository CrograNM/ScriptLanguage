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
#print(L)

count = []
end = 0
for l in L:
    if end <= l[0]:
        end = l[1]
        count.append(l)
#print(count)
print(len(count))