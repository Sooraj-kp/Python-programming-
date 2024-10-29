list=[]
a=0
b=1
size=int(input("Enter length of Fibanacci :"))
for i  in range(size):
    list.append(a)

    a,b=b,a+b
print("the series are:",list)
