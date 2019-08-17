# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
##44점
'''
시간복잡도... 실행 시간을 최대한 단축시켜야 한다.
이 파이썬 코드로 종류2까지 정답처리되고 나머지는 시간초과였는데,
시간을 단축시키기 위해 c코드로 변환 시키는 작업을 해보았지만 sqrt함수를 사용할 수 없고...
함수를 직접 정의하면 오차범위가 생겨 정답이 맞지 않는 문제가 있었다.
그래서 걍 44점으로 제출
'''
A, B = map(int, input().split())

def count_factors(num):
    loop=num**0.5
    # for square number
    if loop==int(loop):
        count=1
    else:
        count=0
    i=1
    while i<loop:
        if num%i==0:
            count+=2
        i+=1
    return count

cnt = 0
for n in range(A,B+1):
    cnt = cnt + count_factors(n)

print(cnt)
