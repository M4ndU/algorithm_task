# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

N = int(input())
h_data = list(map(int, input().split()))

front = h_data[0]
back = h_data[0]

for i in range(2, N):
	front = back
	back = h_data[i]
	if front > back:
		print("NO")
		break
	if i == N-1:
		print("YES")
