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
