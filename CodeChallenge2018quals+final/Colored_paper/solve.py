# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

answer = []

T = int(input()) #TestCase

for i in range(0, T):
	background = [[0]*100 for i in range(100)] #init background_white_paper 100x100 array
	count = 0 # 색종이가 덮고 있는 부분 개수

	NoP = int(input()) #Number of colored_Paper
	paper = [[0]*2 for i in range(NoP)] #init colored paper[distance from left wall][distance from bottom]
		
	for j in range(0, NoP):
		paper[j] = list(map(int, input().split()))
	
	#paper가 흰색 도화지에서 차지하는 모든 좌표값에 1로 표시
	for k in range(0, NoP):
		for y in range(paper[k][0]-1, paper[k][0]+9):
			for x in range(paper[k][1]-1, paper[k][1]+9):
				background[x][y] = 1
				
	#흰색 도화지의 100x100크기의 좌표평면에서 1로 표시된 좌표의 개수를 구함			
	for back_y in range(0, 100):
		for back_x in range(0, 100):
			if background[back_x][back_y] == 1:
				count = count + 1
	#개수 = 넓이, 답안 array에 추가			
	answer.append(count)
	
#모든 답 출력
for i in range(0, T):
	print(answer[i])
