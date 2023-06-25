#https://softeer.ai/practice/info.do?idx=1&eid=407

import sys

k,p,n = map(int,sys.stdin.readline().split())

std = 1000000007
num = k%std

for _ in range(n):
    num = num*p%std
print(num)

