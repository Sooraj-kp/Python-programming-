list=[]
dict={}
size=int(input("ENTER NUMBER OF FIRSTNAMES TO BE ADDED  : "))
for i in range(size):
    fnames=input(f"ENTER FIRST NAME{i+1}:")
    list.append(fnames)
for i in  list:
    count=i.lower().count("a")
    dict[i]=count
print("FIRST NAMES :",list)
print('NUMBER OF OCCURANCE OF "a"',dict)
