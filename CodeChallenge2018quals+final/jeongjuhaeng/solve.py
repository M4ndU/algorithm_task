# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a = int(input())
b = list(map(int, input().split()))

maximun = b[0]
minimun = b[0]

for data in b:
	if maximun < data:
		maximun = data
	if minimun > data:
		minimun = data


if(maximun - minimun + 1 == a):
	print("YES")
else:
	print("NO")
