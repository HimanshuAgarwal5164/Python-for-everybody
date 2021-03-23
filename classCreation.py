class Club:
    counter=0
    def __init__(self,a,b,c):
        self.name=a
        self.age=b
        self.gender=c
        Club.counter=Club.counter+1
        return
    def Price(self):
        if self.age < 18 or self.age > 75:
            print("Not eligible")
            price="Not eligible"
            exit
        elif self.age > 60:
            if self.gender == "male":
                price=7500
            else:
                price=6000
        else:
            if self.gender == "male":
                price=10000
            else:
                price=8500
        return price
    def ShowInfo(self,price):
        if self.gender=="male":
            print("\nWelcome Mr."+self.name+" to our club. Your monthly subscriptions amounts to Rs",price)
        elif self.gender=="female":
            print("\nWelcome Ms."+self.name+" to our club. Your monthly subscriptions amounts to Rs",price)
        else:
            print("\nWelcome "+self.name+" to our club. Your monthly subscriptions amounts to Rs",price)
        return
    @classmethod
    def CounterScore(cls):
        print("\t\t\tCounter reads",cls.counter)





name=input("Enter your name:\t")
age=int(input("Enter your age: \t"))
gender=input("What is your gender?\nEnter \n1 for Male\n2 for Female\n3 for Others:\t")
if gender=='1':
    gender="male"
elif gender=='2':
    gender="female"
else:
    gender="transgender"

p=Club(name,age,gender)
price=p.Price()
if price!="Not eligible":
    p.ShowInfo(price)
    p.CounterScore()

    

            
