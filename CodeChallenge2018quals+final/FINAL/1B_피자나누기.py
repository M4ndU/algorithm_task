# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

#14/50point
answer = []

T = int(input())

for i in range(0, T):
	N = int(input())
	R = list(map(int, input().split()))
	
	if N == 1:
		count = 0
		
	else:
		max_index = 0
		for num in range(N):
			if R[num] > R[max_index]: 
				max_index = num
		high = R[max_index]
		
		if high > 50:
			count = 0
		
		elif high == 50:
			count = 1
			
		else:
			count = 2
		
		
		
	answer.append(count)
	
for j in range(0, T):
	print(answer[j])
