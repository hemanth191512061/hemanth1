z=int(input(""))
if(z<=1000):
 for k in range(2,z):
    if z%k==0:
        print("no")
        break
    else:
        print("yes")
        break
else:
    print("no")
    
        
