def conv(a):
    res=""
    while a!=0:
        if a%2==0:
            res+='0'
        else:
            res+='1'
        a=a//2
    return res[::-1].zfill(4)
def convert(s):
    ans=""
    for i in s:
        if i=='1':
            ans+='0'
        else:
            ans+='1'
    return ans
def add1(s):
    carry=1
    res=""
    for i in range(len(s)-1,-1,-1):
        if s[i]=='1' and carry==1:
            res='0'+res
            carry=1
        elif s[i]=='0' and carry==1:
            res='1'+res
            carry=0
        else:
            res=s[i]+res
    return res
def add_bin(a,b):
    i=len(a)-1
    j=len(b)-1
    res=""
    carry=0
    while i>=0 or j>=0 or carry:
        num1=int(a[i]) if i>=0 else 0
        num2=int(b[j]) if j>=0 else 0
        total=num1+num2+carry
        res=str(total%2)+res
        carry=total//2
        i-=1
        j-=1
    return res
a=int(input())
b=int(input())
bin_1=conv(a)
bin_2=conv(b)
print(add1(convert(bin_1)))
print(add1(convert(bin_2)))
print(add_bin(bin_1,bin_2))
