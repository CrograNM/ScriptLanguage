
def insertion_sort(array):
    for i in range(1, len(array)):  # 카드를 순서대로 뽑는 행위
        for j in range(i, 0, -1):   # 정렬된 부분 중 어느 곳에 삽입할지 선택,
                                    # 인덱스 i부터 1까지, 1씩 감소하며 반복
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    print(array)

array = [1,3,5,7,2,4,6,8,9]
insertion_sort(array)