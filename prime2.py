a=int(input(""))
b=int(input(""))
for c in range(a+1,b):
    
     for d in range(2,c):
        if(c%d)==0:
            break
     else:
            print(c,end=' ')
            
       
    
