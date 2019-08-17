# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# 달팽이 배열을 생성. 그후 원소를 찾아 위치 반환
# 달팽이 배열 생성 코드 : https://tibyte.kr/247
#100점

n, K = map(int, input().split())
k = K-1
board = []
for y in range(0, n):
    for x in range(0, n):
        p = min(x,y,n-x-1,n-y-1)
        if x>=y:
            q = x+y - 2*p
        else:
            q = (n-1 - 2*p)*4 - (x+y - 2*p)
        q += 4 * (p*n - (p*p))
        board.append(q)

if (board.index(k) + 1) % n == 0:
    print(n, (board.index(k) + 1) // n)
else :
    print((board.index(k) + 1) % n , (board.index(k) + 1) // n +1)
