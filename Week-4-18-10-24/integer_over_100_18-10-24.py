list=[]
size=int(input("ENTER NUMBER OF INTEGER TO BE ADDED :"))
for i in range(size):
               integers=int(input(f"ENTER INTEGER {i+1}: "))
               list.append(integers)
for i in range(len(list)):
               if list[i]>100:
                   list[i]='over'
print(list)
                                  
