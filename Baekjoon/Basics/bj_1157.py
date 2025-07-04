# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
#
# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

word = input().lower() #입력 즉시 lowercase화
countList = [0] * 26 #알파벳 개수 센 거 저장하는 리스트
for letter in word:
    countList[ord(letter) - ord('a')] += 1 #ord : 문자를 해당 문자에 대응하는 ascii 코드값으로 변환해줌

maxCount = max(countList)
if countList.count(maxCount) > 1:
    print("?")
else:
    print(chr(countList.index(maxCount) + ord('A')))