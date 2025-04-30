"""
    6 11 : 아래 기상 이미지의 행과 열
    #####.#####
    ####.####.#
    ###..##.#.#
    ##...######
    ######.....
    ###########
    4 : 폭풍을 결정하는 크기
    (북동, 북, 북서, 동, 서, 남동, 남, 남서 ) 끼리 이웃임.
"""

H, W = map(int, input().split())
graph = [list(input()) for _ in range(H)]
K = int(input())
sizes = []

count = 0
def dfs(x, y):
    global count
    if x <= -1 or x >= H or y <= -1 or y >= W:
        return False
    if graph[x][y] == '.':
        count += 1
        graph[x][y] = '#'

        dfs(x-1, y) # 서
        dfs(x, y-1) # 북
        dfs(x+1, y) # 동
        dfs(x, y+1) # 남
        dfs(x + 1, y - 1)  # 북동
        dfs(x - 1, y - 1)  # 북서
        dfs(x + 1, y + 1)  # 남동
        dfs(x - 1, y + 1)  # 남서
        return True
    return False

for i in range(H):
    for j in range(W):
        if dfs(i,j) == True:
            sizes.append(count)
            count = 0

# print(result)
# print(sizes)

# K가 넘는 걸 sizes 에서 골라서 출력
# 가장 큰 sizes 를 출력
num = 0
max = -1000000
for x in sizes:
    if x > K:
        num += 1
    if x >= max:
        max = x

print(num, max)