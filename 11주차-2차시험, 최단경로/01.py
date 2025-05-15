"""
    정렬 3개씩 묶으면 금방 해결
    내림차순, 세번째마다 더하지 않는다
"""

N = int(input()) # 4
array = []
# array.append(0)
for _ in range(N):
    array.append(int(input()))

array = sorted(array, reverse=True)
#print(array)

i = 0
pay = 0
for j in range(N):
    if (j+1) % 3 != 0:
        pay += array[j]
    i += 1

print(pay)
