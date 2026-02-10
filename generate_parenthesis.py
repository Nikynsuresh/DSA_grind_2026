def generateParentheses(n):
    #code here
    res=[]
    def back(o,c,s):
        if len(s)==n:
            res.append(s)
            return
        if o<n//2:
            back(o+1,c,s+"(")
        if c<o:
            back(o,c+1,s+")")
    back(0,0,"")
    return res
n=int(input())
print(generateParentheses(n))
