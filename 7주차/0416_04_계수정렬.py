
def counting_sort(array):
    count = [0] * (max(array) + 1)

    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')
    pass

array = [5,7,11,3,46,2,1,1,4,13,16]
counting_sort(array)