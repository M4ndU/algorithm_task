# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

total = 0 #이 변수에 탑승할 수 있는 회원의 몸무게의 합을 출력한다
count = 0 #이 변수에 탑승할 수 있는 사람의 수를 출력한다

n, p, q = map(int, input().split())
data = list(map(int, input().split()))

for i in range(0, n):
	if data[i] <= p:
		count = count + 1
		total = total + data[i]

print(str(count)+" "+str(total))

if total > q:
	print("NO")
else:
	print("YES")
