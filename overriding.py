class Parent:
    def __init__(self,n):
        self.name=n
        return
    def Hello(self):
        print("Hello",self.name)
        return

class Child(Parent):
    def Hello(self):
        print("Hello %s, How are you?"%(self.name))
        return



p=Parent("Himanshu")
p.Hello()
c=Child("Himanshu Agarwal")
c.Hello()
