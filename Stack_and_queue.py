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
//queue using deque//
from collections import deque
m=[]
que=deque()
for i in range(2,9):
    que.appendleft(i)
print(que)
for j in range(len(que)):
    a=que.popleft()
    print(a)
