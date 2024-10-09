string=input("Enter a string:")
vowels=['a','e','i','o','u','A','E','I','O','U']
list=[]
for i in string:
    if(i in vowels):
        list.append(i)
if list:
    print("vowels are :",list)
else:
    print("no vowels present")
