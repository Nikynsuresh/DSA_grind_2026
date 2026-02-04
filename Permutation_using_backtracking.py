class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        final=[]
        def backtrack(current,remin):
            if len(remin)==0:
                final.append(current[:])
                return
            for i in range(len(remin)):
                new_curr=current+[remin[i]]
                new_rem=remin[:i]+remin[i+1:]
                backtrack(new_curr,new_rem)
        backtrack([],nums)
        return final
print(permute([1,2,3]))
