list=[]
size=int(input("ENTER NUMBER OF  COLOURS:"))
for i in range(size):
    colours=input(f"ENTER COLOUR {i+1}:")
    list.append(colours)
newlist=[list[0],list[-1]]
print("LIST OF COLOURS :",list)
print("NEW LIST :",newlist)
