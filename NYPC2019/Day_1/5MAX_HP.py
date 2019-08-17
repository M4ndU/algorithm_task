# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#100점

H, T = map(int, input().split())
type = [0]*T
hp = [0]*T
for i in range(T):
    type[i], hp[i] = map(int, input().split())

for j in range(T):
    if type[j] == 1:
        H = H - hp[j]
    if type[j] == 2:
        if hp[j] == 0:
            break
        else :
            H = H + hp[j]
    if type[j] == 3:
        H = H + hp[j]
        break
print(H)
