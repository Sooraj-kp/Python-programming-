class fruits:
    def eat(self):
        print("we can eat Fruits ")
class orange(fruits):
    pass
class Apple(fruits):
    def eat(self):
        print("Apple is sweet")
org1=orange()
app1=Apple()
org1.eat()
app1.eat()

   
