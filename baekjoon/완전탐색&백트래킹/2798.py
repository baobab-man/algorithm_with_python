# 블랙잭
# 카지노에서 제일 인기 있는 게임 블랙잭의 규칙은 상당히 쉽다. 카드의 합이 21을 넘지 않는 한도 내에서, 카드의 합을 최대한 크게 만드는 게임이다.
# 블랙잭은 카지노마다 다양한 규정이 있다.
# 한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
# 김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다.
# 그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다. 그런 후에 딜러는 숫자 M을 크게 외친다.
# 이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. 블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.
# N장의 카드에 써져 있는 숫자가 주어졌을 때, M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
# 첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.
# 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.

# solution 1
import sys
N, M = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
num = len(cards)
sum = 0
for i in range(num-2):
    for j in range(i+1, num-1):
        for k in range(j+1, num):
            if cards[i] + cards[j] + cards[k] > M:
                continue
            else:
                sum = max(sum, cards[i]+cards[j]+cards[k])
print(sum)

# solution 2
import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(N):
    for j in range(N):
        for k in range(N):
            if arr[i] + arr[j] + arr[k] > M:
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])
print(result)

# solution 3
from itertools import combinations
import sys
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
for cards in combinations(arr, 3):
    temp_sum = sum(cards)
    if result < temp_sum <= M:
        result = temp_sum
print(result)

# solution 4
n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(i+2, n):
            if cards[i] + cards[j] + cards[k] <= m:
                result = max(result, cards[i] + cards[j] + cards[k])
print(result)

# solution 5
n, m = map(int, input().split())
card = list(map(int, input().split()))
result = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            summ = card[i] + card[j] + card[k]
            if summ <= m:
                result.append(summ)
print(max(result))

# solution 6
n, m = map(int, input().split())
cards = list(map(int, input().split()))
result = list()
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            result.append(sum([cards[i], cards[j], cards[k]]))
result = [i for i in result if i <= m]
if len(result) > 0:
    print(max(result))

# solution 7
n, m = map(int, input().split())
cards = list(map(int, input().split()))
arr = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if cards[i]+cards[j]+cards[k] <= m:
                arr.append(cards[i]+card[j]+cards[k])
print(max(arr))
