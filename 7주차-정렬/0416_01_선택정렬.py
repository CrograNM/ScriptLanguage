
array = [1,3,5,7,2,4,6,8,9]

def selection_sort(array):
    for i in range(len(array)):  # i = 0,1,2,3,,,,len(array)-1
        min_index = i  # 가장 작은 원소의 인덱스
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    print(array)
    pass

selection_sort(array)
