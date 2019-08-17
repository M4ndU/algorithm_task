# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 100점

N = int(input())
HAVE = list(map(int, input().split()))
NEED = list(map(int, input().split()))

MAX = [0] * N

for i in range(N):
    if NEED[i] == 0: # 0으로 나눌 경우 문제가 생긴다. 101개 이상은 만들 수 없으므로 101로 설정해두어 나중에 거르는 값이 되게 한다.
        MAX[i] = 101
    else:
        MAX[i] = HAVE[i] // NEED[i]
a = MAX[0]
for j in range(len(MAX)):
    if a > MAX[j]:
        a = MAX[j]
print(a)
