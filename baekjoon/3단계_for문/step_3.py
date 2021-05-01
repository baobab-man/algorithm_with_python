# 3-1
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 9보다 작거나 같다.
# 출력형식과 같게 N*1부터 N*9까지 출력한다.

a = int(input())
for i in range(1, 10):
    print("{} * {} = {}".format(a, i, a*i))


# 3-2
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 A+B를 출력한다.

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    print(a + b)


# 3-3
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.
# 1부터 n까지 합을 출력한다.

n = int(input())
sum = 0
for i in range(1, n+1):
    sum = sum + i
print(sum)


# 3-4
# 첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.
# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.
import sys

t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)


# 3-5
# 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.
# 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.

a = int(input())
for i in range(a):
    print(i+1)