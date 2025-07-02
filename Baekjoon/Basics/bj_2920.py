# 문제
# 다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.
#
# 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
#
# 연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.
#
# 출력
# 첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.

a = list(map(int, input().split()))
if a[0] < a[1]:
    result = "ascending"
else :
    result = "descending"
for i in range(1,len(a)-1):
    if result == "ascending":
        if a[i+1] > a[i]:
            continue
        else:
            result = "mixed"
            break
    if result == "descending":
        if a[i+1] < a[i]:
            continue
        else:
            result = "mixed"
            break
print(result)

## 몇 개의 값이 들어오든 대응 가능하도록 코드를 짰지만, 8개의 값이 입력으로 들어온다고 정의된 경우
## [1,2,3,4,5,6,7,8]과 [8,7,6,5,4,3,2,1]과 입력값을 비교하고, 같다면 각각 ascending/descending으로 출력
## 둘 중 일치하는 list가 없다면 mixed로 출력하도록 하는 게 나을듯