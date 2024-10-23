string=input("ENETER A STRING :")
first=string[0]
res=first+string[1:].replace(first,'$')
print(res)
