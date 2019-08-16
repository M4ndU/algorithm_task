# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

#55/100point

T = int(input())
answer = []

for i in range(T):
	sum1 = 0
	
	N, M, K = map(int, input().split())
	L = list(map(int, input().split()))
	
	max_L = 0
	for num in range(N):
		if L[num] > L[max_L]: 
			max_L = num
	m = L[max_L]
	
	for i in range(N):
		sum1 = sum1 + L[i]
	
	req = 3 * K + sum1
	sup = N * M
	count = req // sup + 1
	
	if m > count * M:
		count = m // M + 1
	
	answer.append(count)
	
for j in range(0, T):
	print(answer[j])
