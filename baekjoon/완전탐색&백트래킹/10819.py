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

# solution 4

import sys
from itertools import permutations

num = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
answer = 0
members = permutations(array, num)

for member in members:
    member = list(member)
    sum = 0
    for i in range(num-1):
        sum += abs(member[i] - member[i+1])
    answer = max(sum, answer)
print(answer)

# solution 5

"""library 사용 풀이"""
from itertools import permutations
import sys

"""주어진 값 입력"""
num = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

"""permutation 저장"""
per = permutations(array)
answer = 0

"""순열마다 차이를 더해(s), answer보다 크면 answer를 update"""
for i in per:
    s = 0
    for j in range(len(i)-1):
        s += abs(i[j]-i[j+1])
    if s > answer:
        answer = s
print(answer)

# solution 6

import sys


def next_permutation(array):
    k = -1
    m = -1

    # 증가하는 마지막 부분을 가리키는 index k 찾기
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            k = i

    # 전체 내림차순일 경우, 반환
    if k == -1:
        return [-1]

    # index k 이후 부분 중 값이 k보다 크면서 가장 멀리 있는 index m 찾기
    for i in range(k, len(array)):
        if array[k] < array[i]:
            m = i

    # k와 m의 값 바꾸기
    array[k], array[m] = array[m], array[k]

    # k index 이후 오름차순 정렬
    array = array[:k+1] + sorted(array[k+1:])
    return array

# 주어진 값 입력 & 정렬
num = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()

ans = 0
# 첫 순열 내 값 차이를 더해(s), ans 보다 크면 ans를 update
s = 0
for j in range(len(a)-1):
    s += abs(a[j] - a[j+1])
if s > ans:
    ans = s

arr = a

while True:
    arr = next_permutation(arr)
    if arr == [-1]:
        break
    s = 0

    # 순열마다 차이를 더해(s), ans 보다 크면 ans를 update
    for j in range(len(arr)-1):
        s += abs(arr[j]-arr[j+1])
    if s > ans:
        ans = s

print(ans)

# solution 7
import sys
from itertools import permutations

num = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

result = []
for p in permutations(array, num):
    tmp = 0
    for i in range(num-1):
        tmp += abs(p[i]-p[i+1])
    result.append(tmp)

print(max(result))
