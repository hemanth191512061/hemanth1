z=int(input(""))
sum=0
rem=0
k=z
while k>0:
    rem=k%10
    sum=sum*10+rem
    k=k//10
if(sum==z):
    print("yes")
else:
    print("no")
