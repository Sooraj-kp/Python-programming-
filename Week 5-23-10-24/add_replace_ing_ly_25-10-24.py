string=input("Enter string :")
if string[-3:]=='ing':
    string=string[:-3]+'ly'
else:
    string=string=string+"ing"
print(string)