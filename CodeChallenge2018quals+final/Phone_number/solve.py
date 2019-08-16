# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input()) #전화번호의 수 
data = [] # 각 전화번호의 뒷자리 
for i in range(n):
	num = int(input())
	data.append(num)
	
cnt = [0] * 10000 #cnt[XXXX] := 뒷 자리가 XXXX인 전화번호의 수 

for d in data:
	cnt[d] = cnt[d] + 1


max_index = 0 #가장 많이 등장한 뒷자리 후보 
for num in range(10000): #모든 뒷자리에 대하여 
	if cnt[num] > cnt[max_index]: 
		max_index = num

print("%04d" % max_index ) 
