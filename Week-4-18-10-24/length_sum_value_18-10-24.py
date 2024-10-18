list1=[1,2,3,4,5]
list2=[2,3,4,5,9]
if(len(list1)==len(list2)):
    print("list is equal ")
else:
    print("list is not equal")
if(sum(list1)==sum(list2)):
    print("sum is equal")
else:
    print("sum is not equal")
common_number=set(list1).intersection(set(list2))
if common_number:
    print("Common number : ", common_number)
else:
    print("no common number")
