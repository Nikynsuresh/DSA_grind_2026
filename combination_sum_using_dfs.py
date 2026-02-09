#Combination sum 1
def combination(candidates,target):
    res=[]
    def dfs(start,total,path):
        if total==target:
            res.append(path[:])
            return
        if total>target:
            return
        for i in range(start,len(candidates)):
            path.append(candidates[i])
            dfs(i,total+candidates[i],path)
            path.pop()
    dfs(0,0,[])
    return res
print(combination([2,3,5,7],7))
#Combination sum 2(with unique values)
def combination2(arr,target):
    ans=[]
    arr.sort()
    def dfs(start,path,total):
        if total==target:
            ans.append(path[:])
        if total>target:
            return
        for i in range(start,len(arr)):
            if i>len(arr) and path[i]==path[i-1]:
                continue
            path.append(arr[i])
            dfs(i+1,path,total+arr[i])
            path.pop()
    dfs(0,[],0)
    return ans
print(combination2([10,3,4,2,5,8],5))
