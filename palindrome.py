n=int(input("enter the input"))
sum=0
rem=0
k=n
while k>0:
    rem=k%10
    sum=sum*10+rem
    k=k//10
if(sum==n):
    print("yes")
else:
    print("no")
