x=int(input(""))
sum=0
rem=0
k=x
while k>0:
    rem=k%10
    sum=sum*10+rem
    k=k//10
if(sum==x):
    print("yes")
else:
    print("no")
