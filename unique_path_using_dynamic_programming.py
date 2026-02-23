class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
#uses the technique that ways to reach current cell=ways to reach left cell+ways to reach right cell
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
        dp=[[0]*c for i in range(r)]
        dp[0][0]=1 if obstacleGrid[0][0]==0 else 0
        for i in range(r):
            for j in range(c):
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                else:
                    if i>0:
                        dp[i][j]+=dp[i-1][j]
                    if j>0:
                        dp[i][j]+=dp[i][j-1]
        return dp[r-1][c-1]
#same unique path with obsctacle 1 represents as obstacles
