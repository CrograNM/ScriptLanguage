"""
    프로그래머스 - 정수 삼각형
"""
"""
    아래 칸으로 이동해서 거쳐간 숫자의 합이 가장 큰 경우를 찾기
    아래칸으로 이동할 때는 대각선 방향으로 한칸 오른쪽 또는 왼쪽으로만 이동 가능
    [7]                 tri[0][0]
    [3  8]              tri[1][0]   # 왼쪽으로 내려가면 j값이 안변함
    [8  1   0]          tri[2][0]   
    [2  7   4   4]      tri[3][1]   # 오른쪽으로 내려가면 j값 +1
    [4  5   2   6   5]  tri[4][0]   7-3-8-7-5 -> 30
    
    dp[i][j] => i레벨 j번째 노드까지 경로의 최대값이라고 하자. 
                루트 노드는 트리 전체 경로의 최대값이 된다
    dp[i][j] = triangle[i][j] + max( dp[i+1][j], dp[i+1][j+1] )
    triangle[i][j] = triangle[i][j] + max( triangle[i+1][j], triangle[i+1][j+1] )
"""

def solution(triangle):
    L = len(triangle) # 트리 레벨

    for i in range(L-2, -1, -1):        # i = L-2, L-3, ..., 1, 0
        for j in range(len(triangle[i])):  # i레벨 노드의 개수 = 서브트리의 개수
            triangle[i][j] = triangle[i][j] + max( triangle[i+1][j], triangle[i+1][j+1] )

    return triangle[0][0] # 루트 노드에 가장 큰 경로가 저장되게 된다


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
# 30