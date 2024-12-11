class employee:
    company_name="ABC COMPANY"
    location="CALICUT"
    def __init__(self,id,name,salary):
        self.id=id
        self.name=name
        self.salary=salary

    def details(self):
        print(self.id,self.name,self.salary)


            
emp1=employee(101,"JYOTHISH",75000)
emp2=employee(102,"JANIB",1000000)




emp1.details()
emp2.details()
