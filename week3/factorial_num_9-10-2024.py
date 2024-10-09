n=int(input("Enter the number n:"))
factorial=1
if(n<0):
    print("NO factorial  for  negative number:")
elif(n==0):
    print("factorial = ",1)
else:
    for i in range (1,n+1):
        
        factorial=factorial*i
    print("factorial =",factorial)
    
