grid=[[0,1,1,0],
[0,0,0,0],
[0,0,1,0],[1,1,1,0]]
r,c=len(grid),len(grid[0])
sol=[[0]*c for i in range(r)]
def backtrack(i,j,sol):
    if i==r-1 and j==c-1 and grid[i][j]==0 and sol[i][j]==0 :
        sol[i][j]=1
        return True
    elif i<0 or j<0 or i>=r or j>=c or grid[i][j]==1:
        return False
    if sol[i][j]==1:
        return False
    sol[i][j]=1
    if backtrack(i+1,j,sol):
        return True
    if backtrack(i,j+1,sol):
        return True
    if backtrack(i-1,j,sol):
        return True
    if backtrack(i,j-1,sol):
        return True
    sol[i][j]=0
    return False
print(backtrack(0,0,sol))
for i in sol:
    print(i)
