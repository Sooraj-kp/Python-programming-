def fibonacci(n):
    list1=[]
    a=0
    b=1
    for i in range(n):
        list1.append(a)
        a,b=b,a+b
        
    return list1

n=int(input("Enter the number of terms: "))
print("Fibonacci series:",fibonacci(n))