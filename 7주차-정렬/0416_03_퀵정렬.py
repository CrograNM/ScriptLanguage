
def quick_sort(array, start, end):
    if start >= end:    # 원소가 1개인 경우
        return
    pivot = start       # 피벗은 첫번째 원소
    left = start + 1
    right = end
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right):   # 엇갈렸다면 작은 데이터와 피벗를 교체
            array[right], array[pivot] = array[pivot], array[right]
        else:               # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
    pass

array = [1,3,5,7,2,4,6,8,9]
quick_sort(array, 0, len(array)-1)
print(array)

def quick_sort_py(array):
    if len(array) <= 1:
        return array

    pivot = array[0]    # 피벗은 첫번째 원소
    tail = array[1:]    # 피벗을 제외한 리스트

    left_side = [ x for x in tail if x <= pivot ]   # 분할된 왼쪽 부분
    right_side = [ x for x in tail if x > pivot ]   # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)

array2 = [5,7,11,3,46,2,1,13,16]
print(quick_sort_py(array2))