string=input("Enter string : ")

if len(string)>=2:
    string=string[-1]+string[1:-1]+string[0]
    print("After swap ",string)
else:
    print("swapping is not possible ") 
