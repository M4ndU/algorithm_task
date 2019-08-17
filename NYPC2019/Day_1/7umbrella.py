# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#100점

N, M, BZ = map(int, input().split())

B = [0]*M
R = [0]*M
for i in range(M):
    B[i], R[i] = map(int, input().split())

imhere = BZ
have = [0]* (N+1)
buy = 0
for j in range(M):
    if R[j] == 1:
        if have[imhere] == 0: #현재 건물에 우산이 없다.
            buy = buy +1
            have[B[j]] = have[B[j]] + 1 #처음에 우산 두개 이상 보관하는 것을 생각을 못해서 '일부 오답'이 나왔었다.
        else : # 현재 건물에 우산이 있다.
            have[imhere] = have[imhere] - 1
            have[B[j]] = have[B[j]] + 1
    imhere = B[j]
print(buy)
