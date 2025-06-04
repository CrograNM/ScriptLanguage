"""
    TUK 0001 - 소수회문
"""
"""
    주어진 정수와 그 정수를 reverse한 정수가 서로 같으면 그 정수는 회문(Palindrome)이라고 합니다.. 예를 들어 79197 및 324423은 Palindrome입니다.

    정수 N(1 ≤ N ≤ 1000000)이 하나 주어지고,  
    M이 소수(prime number)이고 Palindrome이되는 가장 작은 정수 M (M ≥ N)을 찾습니다.
    M은 N보다 크거나 같습니다.

    M이 소수(prime number)이므로 M은 1과 M으로만 나누어 떨어져야 합니다.
    예를 들어, N이 31이면 답 M은 101입니다.
"""
def isPrime(x):
    if x <= 0 or x == 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def isPalindrome(x):
    # int -> str
    string_number = str(x)
    return string_number == string_number[::-1]

N = int(input())
M = N
while True:
    if isPalindrome(M):
        if isPrime(M):
            print(M)
            break
    M += 1