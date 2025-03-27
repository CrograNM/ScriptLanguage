from collections import deque
print("\n스택 구현 예제")
stack = [] # 리스트 대신 deque를 사용해도 된다. (속도가 빠름)
stack.append(5)
stack.append(1)
stack.append(3)
print(stack)
stack.pop()
print(stack)
stack.pop()

print("\n큐 구현 예제")
# from collections import deque
queue = deque()
