digits=input().strip()
numpad={'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
if digits=="" or digits=="1":
    print("No Combination")
else:
    ans=[]
    def back(ind,path):
        if ind==len(digits):
            ans.append(path)
            return
        curr=digits[ind]
        for ch in numpad[curr]:
            back(ind+1,path+ch)
    back(0,"")
    print(*ans)
