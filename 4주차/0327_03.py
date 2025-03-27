""" 재귀 함수 """

""" 무한한 재귀 호출 : 재귀 깊이 초과 오류가 나며 종료 된다 """
# def recursive_func():
#     print("재귀 호출")
#     recursive_func()

""" 재귀 함수의 종료 조건을 잘 설정해 주어야 한다. """
# def recursive_func(i):
#     if i == 100:
#         return
#     print(i,"번째 함수에서", i+1, "번째 재귀 함수 호출")
#     recursive_func(i+1)
#     print(i, "번째 재귀 함수를 종료합니다")
# recursive_func(1)

""" 팩토리얼 구현 예제 """
def factorial_iterative(N):
    result = 1
    
    # 1부터 N까지의 수를 차례대로 곱하기
    for i in range(1, N + 1):
        result *= i
    return result

def factorial_recursive(N):
    if N <= 1: # N이 1 이하인 경우 1을 반환
        return 1
    # N! = N * (N-1)!를 그대로 코드로 작성
    return N * factorial_recursive(N - 1)

# 각각의 방식으로 구현한 N! 출력
print("반복적으로 구현 : ", factorial_iterative(5))
print("재귀적으로 구현 : ", factorial_recursive(5))