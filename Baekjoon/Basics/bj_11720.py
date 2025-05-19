# 문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.
#
# 출력
# 입력으로 주어진 숫자 N개의 합을 출력한다.

howMany = int(input())
numbers = input()
sum = 0;

# 그냥 간단하게 string을 하나씩 돌면서 더하는 방식으로 해결
for i in numbers:
    sum += int(i)
print(sum)