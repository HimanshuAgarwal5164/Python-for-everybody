class Salary:
    def __init__(self,n,sal,o):
        self.name=n
        self.salary=sal
        self.overtime=o
        return
    def Total(self):
        total=self.salary+self.overtime
        return total
    def Display(self,total):
        print("Hello {}, Collect your paycheck amounting to Rs{} as soon a possible".format(self.name,total))
        return



class NewSalary(Salary):
    def __init__(self,n,sal,o,inc):
        super().__init__(n,sal,o)
        self.incentive=inc
        return
    def Total(self):
        total=self.salary+self.overtime+self.incentive
        return total






s=Salary("Kalpit",101,101)
total=s.Total()
s.Display(total)
n=NewSalary("Himanshu",1000000000000,0,100000000)
total=n.Total()
n.Display(total)
        
