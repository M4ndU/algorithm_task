# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

#30/100 point

T = int(input())
answer = []
r = [0, 0, 0, 1, 3, 6, 10, 15, 21, 28, 36, 42, 46, 48, 48, 46, 42, 36, 28, 21, 15, 10, 6, 3, 1]

for i in range(T):
	N, M = map(int, input().split())
	
	if N <= 2 :
		pn = 8 ** N
	
	else:
		a = 1
		b = 0
		if N > 3:
			a = 8 ** (N - 3)
			
		for j in range(M):
			b = b + r[j]
		c = 8 ** 3 - b
		pn = a * c
	
	count = pn % 1000000007
	
	answer.append(count)
	
for j in range(0, T):
	print(answer[j])
