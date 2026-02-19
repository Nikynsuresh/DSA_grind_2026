size=int(input())
startx=int(input())
starty=int(input())
targetx=int(input())
targety=int(input())
startx-=1
starty-=1
targetx-=1
targety-=1
m=[10000]
sol=[[0]*size for i in range(size)]
def backtrack(x,y,steps,sol):
    if x<0 or y<0 or x>=size or y>=size:
        return 
    if x==targetx and y==targety:
        m[0]=min(m[0],steps)
        return
    if m[0] < steps:
        return
    if sol[x][y] == 1:
        return
    sol[x][y]=1
    backtrack(x+2,y+1,steps+1,sol)
    backtrack(x+2,y-1,steps+1,sol)
    backtrack(x-2,y+1,steps+1,sol)
    backtrack(x-2,y-1,steps+1,sol)
    backtrack(x+1,y+2,steps+1,sol)
    backtrack(x+1,y-2,steps+1,sol)
    backtrack(x-1,y+2,steps+1,sol)
    backtrack(x-1,y-2,steps+1,sol)
    sol[x][y]=0
print(backtrack(startx,starty,0,sol))
print(m[0])
    
