# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#100점

import re

N = int(input())

emails =[]
for i in range(N):
    emails.append(str(input()))


p = re.compile('^[a-zA-Z0-9-.]+@[a-zA-Z0-9-.]+$')

for email in emails:
    if p.match(email):
        print("Yes")
    else :
        print("No")
