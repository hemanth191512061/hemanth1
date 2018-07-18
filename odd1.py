a=int(input(""))
b=int(input(""))
if(b<=100000):
 for c in range(a,b+1):
    if(c%2!=0):
        print(c,end=" ")
else:
    print("no output")
