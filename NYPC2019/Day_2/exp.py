# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#0점

import itertools

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def perm(a):
    length = len(a)
    if length == 1:
        return [a]
    else:
        result = []
        for i in a:
            b = a.copy()
            b.remove(i)
            b.sort()
            for j in perm(b):
                j.insert(0, i)
                if j not in result:
                    result.append(j)
        return result

N = int(input())
exp = [[0]*N for i in range(N)]

for i in range(0,N):
    exp[i] = list(map(int, input().split()))

player = [0]*N
for j in range(0, N):
    for k in range(0, N):
        player[j] = player[j]+ exp[k][j]

S = factorial(N)
base = [0] * N
rank = [[0]*N for i in range(S)]
task = [0]* S

num = N
a = [x for x in range(0, int(num))]
rank = perm(a)


for m in range(0, S):
    for n in range(0, N):
        if n == 0 :
            minus = 0
        else :
            minus = 0
            r= n
            while(r>0):
                minus += exp[rank[m][n]][rank[m][r-1]]
                r -= 1

        task[m] += player[rank[m][n]] -minus

MAX = task[0]
for q in range(0, S):
    if MAX < task[q] :
        MAX = task[q]

print(MAX)
