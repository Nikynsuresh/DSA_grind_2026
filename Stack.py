//stack//
from collections import deque
m=deque()
n=int(input())
for i in range(n):
    m.append(int(input()))
print(m)
arr=[]
for i in range(len(m)):
    x=m.pop()
    arr.append(x)
arr.sort()
for i in range(len(arr)):
    m.append(arr[i])
print(m)
