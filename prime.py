N=int(input(""))
if(N<=1000):
 for k in range(2,N):
    if N%k==0:
        print("no")
        break
    else:
        print("yes")
        break
else:
    print("no")
    
        
