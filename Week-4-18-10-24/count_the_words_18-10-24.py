string=input("enter text: ")
word=input("ENETER THE WORD :")
a=[]
count=0
a=string.split(" ")
for i in range(0,len(a)):
    if (word==a[i]):
        count=count+1
print("COUNT OF THE WORDS IS :",count)
