# 스타트와 링크
# 첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

# solution 1
from itertools import combinations

N = int(input())
ability_board = []
for _ in range(N):
    ability_board.append(list(map(int, input().split())))

num_list = [i for i in range(N)]
res = float('inf')

def solve():
    global res

    # 조합을 이용하여 각 후보자를 생성함
    for cand in combinations(num_list, N//2):
        # 선택된 후보와 나머지
        start_member = list(cand)
        link_member = list(set(num_list) - set(cand))

        # 점수 비교는 2명씩 이루어진다.
        start_comb = list(combinations(start_member, 2))
        link_comb = list(combinations(link_member, 2))

        # 점수 구하기
        start_sum = 0
        for x,y in start_comb:
            start_sum += (ability_board[x][y] + ability_board[y][x])

        link_sum = 0
        for x,y in link_comb:
            link_sum += (ability_board[x][y] + ability_board[y][x])

        # 차이를 구하는 것이므로 abs 사용
        if(res > abs(start_sum - link_sum)):
            res = abs(start_sum - link_sum)

solve()
print(res)

# solution 2

from sys import maxsize
from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
cb = combinations(range(n), n//2)
ans = maxsize

for c in cb:
    a = set(c)
    b = list(set(range(n)) - a)
    a = list(a)

    a_teamwork, b_teamwork = 0, 0

    for i in range(n//2 - 1):
        for j in range(i + 1, n//2):
            a_teamwork += s[a[i]][a[j]] + s[a[j]][a[i]]
            b_teamwork += s[b[i]][b[j]] + s[b[j]][b[i]]

    ans = min(ans, abs(b_teamwork - a_teamwork))

print(ans)

# solution 3

import itertools
import sys

def cal(lines, a, b):
    return lines[int(a)][int(b)]

def bruteforce(lines, n):
    count = n // 2
    members = range(n)
    teams = itertools.combinations(members, count)
    min_result = 9999999

    for team in teams:
        start = set(list(team))
        link = list(members - start)
        start_total = 0
        link_total = 0

        # 조합에 0이 포함되어 있지 않는 부분이 딱 중간 부분
        # (0이 포함되거나, 포함되지 않거나로 반을 나눈다)
        if team[0] != 0:
            break

        start = list(start)
        start_combi = itertools.combinations(start, 2)
        for coms in start_combi:
            start_total += cal(lines, coms[0], coms[1])

        link_combi = itertools.combinations(link, 2)
        for coml in link_combi:
            link_total += cal(lines, coml[0], coml[1])

        if abs(link_total - start_total) < min_result:
            min_result = abs(link_total - start_total)

    return min_result

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    lines = []
    for i in range(n):
        line = list(map(int, sys.stdin.readline().strip().split()))
        lines.append(line)

    # a, b의 값이 정해졌을 때 a-b, b-a의 능력치를 한번만 조회할 수 있도록, 값들을 한곳에 모아둔다.
    for i in range(n):
        for j in range(n):
            if j > i:
                lines[i][j] = lines[i][j] + lines[j][i]
                lines[j][i] = 0
    print(bruteforce(lines, n))

# solution 4

import sys

n = int(sys.stdin.readline())

startlink = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
team = [0 for _ in range[n]]

count = 0
result = 99999999999999
# 팀을 나누는 경우의수
# 팀을 나누고 난 뒤 각각의 차 구해서 최소값찾기
def maketeam(index, j):
    if index == n//2:
        global result
        global count
        start = 0 # 스타트 팀합
        link = 0
        count += 1
        start_list = [] # 담아서 비교
        link_list = []
        for i in range(n):
            if team[i] == 1:
                start_list.append(i)
            else:
                link_list.append(i)

        for i in range(len(start_list)):
            for j in range(len(start_list)):
                start += startlink[start_list[i]][start_list[j]]
                link += startlink[link_list[i]][link_list[j]]
        if start > link:
            if result > start-link:
                result = start-link
        else:
            if result > link-start:
                result = link-start
        return
    else:
        for i in range(j, n):
            if team[i]==0:
                team[i]=1
                maketeam(index+1, i)
                team[i]=0
            else:
                continue
team[0]=1
maketeam(1, 0)
print(result)

# solution 5

import sys

n = int(sys.stdin.readline())
mat = []
for i in range(n):
    mat.append(list(map(int, sys.stdin.readline().strip().split())))

from itertools import combinations
gab = 9999999999
team = [i for i in range(n)]
tt = list(combinations(team, n//2))
for team1 in tt:
    team2 = [x for x in team if x not in team1]
    team1_score = 0
    team2_score = 0
    for x, y in list(combinations(team1, 2)):
        team1_score += mat[x][y] + mat[y][x]
    for x,y in list(combinations(team2, 2)):
        team2_score += mat[x][y] + mat[y][x]
    gab = min(gab, abs(team1_score - team2_score))

print(gab)

