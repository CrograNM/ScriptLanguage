
import heapq

# 오름차순 힙 정렬
def heapsort(iterable):
    h = []      # 최소 힙에 사용될 리스트
    result = [] # 정렬 결과 리스트
    # 모든 원소를 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value) # 대상이 되는 리스트(h)에 value를 차례로 넣는다
    # print(h)
    # 힙에 삽입된 모든 원소를 차례로 꺼내서 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)