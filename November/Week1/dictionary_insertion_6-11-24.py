dict1={'Name':'Sooraj','Roll number':56,'registration number':'MES-MCA2056','department':'MCA','semester':1}
print("Dictionary : ",dict1)
print()

dict1['total mark']=int(input("Enter the total mark out of 100:"))
print()
print("Dictionary after adding total mark:",dict1)
print()

if dict1['total mark']>=90:
    dict1['grade']='A'
    
elif dict1['total mark']>=82:
    dict1['grade']='B'
    
elif dict1['total mark']>=60:
    dict1['grade']='C'
    
elif dict1['total mark']>=50:
    dict1['grade']='p'
else:
    dict1['grade']='F'
print("Dictionary after adding grade:",dict1)
print()

dict1.pop('Roll number')
print("Dictionary after deleting roll number:",dict1)
