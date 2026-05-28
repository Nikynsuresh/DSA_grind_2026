def catch_theif(mat,k):
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    co=0
    row=len(mat)
    col=len(mat[0])
    visit=[[False]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if mat[i][j]=="P":
                caught=False
                for dx,dy in directions:
                    for mov in range(1,k+1):
                        ni=i+dx*mov
                        nj=j+dy*mov
                        if 0<=ni<row and 0<=nj<col:
                            if mat[ni][nj]=="T" and not visit[ni][nj]:
                                co+=1
                                visit[ni][nj]=True
                                caught=True
                                break
                    if caught:
                        break
    return co
matrix = [
    ['P', 'T', 'T'],
    ['T', 'P', 'T'],
    ['T', 'T', 'P']
]
k=1
print(catch_theif(matrix,k))
