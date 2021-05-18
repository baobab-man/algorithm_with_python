# 차이를 최대로(백트래킹)
# N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.
# |A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
# (입력)첫째 줄에 N (3 ≤ N ≤ 8)이 주어진다. 둘째 줄에는 배열 A에 들어있는 정수가 주어진다. 배열에 들어있는 정수는 -100보다 크거나 같고, 100보다 작거나 같다.
# (출력)첫째 줄에 배열에 들어있는 수의 순서를 적절히 바꿔서 얻을 수 있는 식의 최댓값을 출력한다.

# solution 1
from itertools import permutations  # 순열 내장함수
import sys
input = lambda: sys.stdin.readline().strip()

num = int(input())
array = list(map(int, input().split()))

p = list(permutations(array, num))
result = 0

for i in p:
    s = 0
    li = list(i)
    for j in range(1, num):
        s += abs(li[j]-li[j-1])
    result = max(result, s)

print(result)

# solution 2
from itertools import permutations

num = int(input())
array = list(map(int, input().split()))


def sumOf(exp):
    count = 0
    for i in range(len(exp)):
        count += abs(exp[i]-exp[i-1])
    return count

array2 = list(permutations(array, num))
result = []
for i in array2:
    result.append(sumOf(i))

print(max(result))

# solution 3

from itertools import permutations

num = int(input())
array = permutations(list(map(int, input().split())))
result = 0
for a in array:
    sum = 0
    for i in range(num-1):
        sum += abs(a[i]-a[i+1])
    result = max(result, sum)
print(result)
