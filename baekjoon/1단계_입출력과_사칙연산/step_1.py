# 1-1
# Hello World!를 출력하시오.

print("Hello World!")
print('*' * 100)


# 1-2
# 두 줄에 걸쳐 "강한친구 대한육군"을 한 줄에 한 번씩 출력한다.

army = "강한친구 대한육군"
print(army + '\n' + army)
print('*' * 100)


# 1-3
# 고양이를 출력한다.

print("\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \(__)|")
print('*' * 100)


# 1-4
# 개를 출력한다.

print('|\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\__|')
print('*' * 100)


# 1-5
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A+B를 출력한다.

print(sum(map(int, input().split())))
print('*' * 100)


# 1-6
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A+B를 출력한다.

a, b = map(int, input().split())
print(a - b)
print('*' * 100)


# 1-7
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 AxB를 출력한다.

a, b = map(int, input().split())
print(a * b)
print('*' * 100)


# 1-8
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 첫째 줄에 A/B를 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-9 이하이면 정답이다.

a, b = map(int, input().split())
print(a / b)
print('*' * 100)