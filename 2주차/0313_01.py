"""


"""
from itertools import count

x=10
def sum(x,y):
    x=1 # local 변수로서의 x가 1로 바뀐다. 전역변수에는 영향이 없다
    return x + y
print(sum(x,20))

# 그러나 아래와 같은 경우는 change가 wordlist를 변화시킨다.
def change(x): # 리스트를 보낼 경우 레퍼런스로 받아와서, 원본에도 영향이 간다
    x[0] = 'H'
wordlist = ['J', 'A', 'M']
change(wordlist)
print(wordlist)

# global 키워드
a = 0
def func():
    global a    # 전역변수 a를 참조하겠다 선언
    a += 1      # global 키워드가 없으면 전역변수를 사용할 수 없다
for i in range(10):
    func()
print(a)

# 튜플로 리턴값 받아오기 -> cpp는 temporary 변수를 사용해야한다(?)
def operator(a,b):
    return a+b, a-b, a*b, a/b
a,b,c,d = operator(7,3)
print(a,b,c,d)

# 람다 함수
(lambda a,b: a+b)(3,7)
array = [('F',3), ('A',50), ('B',32)]
array.sort() # 기본 sort -> 첫번째 원소 기준 sort
print(array)
array.sort(key=lambda x:x[1]) # lamda 응용 -> sort 기준을 두번째 원소로 변경
print(array)
# array.sort(key=lamda x:(x[1], x[0])

"""
>>> sum([1,2,3]) 
6
>>> min(1,5,10,20,30)
1
>>> max(1,5,10,20,30)
30
>>> eval('(1+4)*7')
35
"""

# 카운터 기능
from collections import Counter
counter = Counter(['red','red','blue','blue','blue'])
print(counter['red'])
print(type(counter))
dict(counter) # 사전 자료형으로 변환 가능
print(counter)