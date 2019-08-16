#어느정도 작동하나, timeout으로 오답처리된 풀이. 어떻게 바꿔야 시간을 줄일 수 있을까?
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

N, M = map(int, input().split())
card_n = list(map(int, input().split()))
win_m = list(map(int, input().split()))

a = [0]*M

for i in range(0, N):
	for j in range(0, N):
		sum_n = card_n[i] + card_n[j]
		
		for k in range(0, M):
			if win_m[k] == sum_n:
				a[k] = 1
				break
				
count = 0
for m in range(0, M):
	if a[m] == 1:
		count = count + 1

print(count)
