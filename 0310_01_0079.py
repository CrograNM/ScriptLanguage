"""
    문자열 폭발 (TUK 0079)

    input : 문자열1, 문자열2(폭발대상 문자열)
    (문자열은 모두 알파벳, 숫자로만 이뤄짐)
    output : 문자열 결과
    
    ->  for문을 통해 폭발시킬 문자열을 없애며 문자열을 재생성,
        만약 재생성된 문자열에 폭발 대상 문자열이 있다면 다시 폭발 후 재생성
        최종적으로 폭발 대상 문자열이 검사되지 않으면 결과 출력
"""

"""
인풋 2개
find 함수 사용 (문자열 찾기 실패시 -1 반환(탈출에 사용))
find 는 시작 인덱스를 반환하므로 시작 인덱스 + 문자열의 길이만큼 삭제
    -> 여러 문자열이 검사되면 첫번째 문자열의 시작 인덱스를 반환

간단한 슬라이싱으로 문자 삭제하는 방법
text = "Hello, World!"
result = text[:5] + text[6:]
print(result)  # 출력 결과: Hello World!
"""

"""
mirkovC4nizCC44
C4

-> mirkovniz
"""

# input 으로 문자열과 폭탄을 받는다
text = input()
boom = input()
boom_len = len(boom)

# for문으로 모든 폭탄이 사라질 때 까지 반복한다
found = 0
while True:
    found = text.find(boom)
    if found == -1:
        print(text) # 더이상 폭탄이 검사가 안되면 출력 및 탈출
        break

    # 코드가 종료되지 않았으면 문자 폭발(슬라이싱)
    temp = text[:found] + text[found+boom_len:]
    text = temp
